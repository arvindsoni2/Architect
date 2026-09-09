"""Check the manual's persistence boundary without a paid provider or database.

This tests connection lifetime and async usage, not PostgreSQL restart durability.
"""
import asyncio
from contextlib import asynccontextmanager, contextmanager
from html.parser import HTMLParser
from pathlib import Path
import os
import sys
import types
import unittest
from unittest.mock import patch


class CodeBlocks(HTMLParser):
    def __init__(self):
        super().__init__()
        self.blocks = []
        self.current = None

    def handle_starttag(self, tag, attrs):
        if tag == 'pre':
            self.current = ''

    def handle_data(self, data):
        if self.current is not None:
            self.current += data

    def handle_endtag(self, tag):
        if tag == 'pre' and self.current is not None:
            self.blocks.append(self.current)
            self.current = None


class PersistenceBoundary(unittest.TestCase):
    def test_documented_pytest_default_excludes_live_provider_tests(self):
        # Exercise pytest's own marker selection using the visible TOML config.
        import tempfile
        import subprocess
        parser = CodeBlocks()
        parser.feed((Path(__file__).resolve().parents[1] / 'handbooks/agent-engineering/agent-engineering-master-manual-v2.7.html').read_text())
        config = next(code for code in parser.blocks if code.startswith('[project]'))
        with tempfile.TemporaryDirectory() as directory:
            Path(directory, 'pyproject.toml').write_text(config)
            Path(directory, 'test_selection.py').write_text(
                'import pytest\n'
                'def test_local(): pass\n'
                '@pytest.mark.live\n'
                'def test_paid_provider(): raise AssertionError("Live provider test selected")\n')
            result = subprocess.run([sys.executable, '-m', 'pytest'],
                                    cwd=directory, text=True, capture_output=True)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn('1 deselected', result.stdout)

    def test_integration_only_invokes_supplied_forge_after_completed_research(self):
        parser = CodeBlocks()
        parser.feed((Path(__file__).resolve().parents[1] / 'handbooks/agent-engineering/agent-engineering-master-manual-v2.7.html').read_text())
        source = next(code for code in parser.blocks if 'def continue_course_lesson(' in code)
        response = {'status': 'awaiting_approval', 'run_id': 'synthetic-run'}

        class Client:
            def __init__(self, url):
                pass
            async def __aenter__(self):
                return self
            async def __aexit__(self, *args):
                pass
            async def call_tool(self, name, arguments, **kwargs):
                return types.SimpleNamespace(data=response)

        class Forge:
            async def ainvoke(self, state):
                return {'draft_sources': state['research_bundle']['sources']}

        module = types.ModuleType('fastmcp')
        module.Client = Client
        with patch.dict(sys.modules, {'fastmcp': module}):
            namespace = {}
            exec(source, namespace)

            async def exercise():
                call = namespace['continue_course_lesson']
                args = dict(topic='Synthetic topic', audience='learner', run_id='synthetic-run', approved=True, forge_graph=Forge())
                pending = await call(**args)
                self.assertEqual(pending['research']['status'], 'awaiting_approval')
                response.update(status='completed', bundle={'sources': ['approved-source']})
                self.assertEqual(await call(**args), {'draft_sources': ['approved-source']})

            asyncio.run(exercise())

    def test_graph_remains_usable_until_async_application_scope_exits(self):
        parser = CodeBlocks()
        parser.feed((Path(__file__).resolve().parents[1] / 'handbooks/agent-engineering/agent-engineering-master-manual-v2.7.html').read_text())
        source = next(code for code in parser.blocks if 'def compile_for_production(' in code)

        class Saver:
            active = False
            ready = False

            @classmethod
            @asynccontextmanager
            async def from_conn_string(cls, url):
                saver = cls()
                saver.active = True
                try:
                    yield saver
                finally:
                    saver.active = False

            async def setup(self):
                self.ready = True

        class SyncSaver:
            @classmethod
            @contextmanager
            def from_conn_string(cls, url):
                yield cls()

        class Graph:
            def __init__(self, saver):
                self.saver = saver

            async def ainvoke(self, value):
                if not self.saver.active or not self.saver.ready:
                    raise RuntimeError('Checkpoint connection is not usable')
                return value

        class Builder:
            def compile(self, *, checkpointer):
                return Graph(checkpointer)

        sync_module = types.ModuleType('langgraph.checkpoint.postgres')
        sync_module.PostgresSaver = SyncSaver
        async_module = types.ModuleType('langgraph.checkpoint.postgres.aio')
        async_module.AsyncPostgresSaver = Saver
        with patch.dict(sys.modules, {'langgraph.checkpoint.postgres': sync_module,
                                     'langgraph.checkpoint.postgres.aio': async_module}), \
             patch.dict(os.environ, {'DATABASE_URL': 'postgresql://synthetic'}):
            namespace = {}
            exec(source, namespace)

            async def exercise():
                async with namespace['compile_for_production'](Builder()) as graph:
                    self.assertEqual(await graph.ainvoke({'request': 'initial'}), {'request': 'initial'})
                    self.assertEqual(await graph.ainvoke({'request': 'resume'}), {'request': 'resume'})
                with self.assertRaisesRegex(RuntimeError, 'not usable'):
                    await graph.ainvoke({})

            asyncio.run(exercise())


if __name__ == '__main__':
    unittest.main()
