// Real browser coverage for the standalone handbook audit regressions.
const {chromium} = require('playwright');
const assert = require('node:assert/strict');
const fs = require('node:fs/promises');
const path = require('node:path');
const {pathToFileURL} = require('node:url');
const root = path.join(__dirname,'..');
const output = process.env.ARCHITECT_SCREENSHOTS || '/tmp/architect-browser-review';
const files = {
  system:'handbooks/system-design/system-design-concept-handbook-v6.html',
  interview:'learning-paths/ai-ml-interview/interview-resource-accelerator-v4.4.html',
  ai:'handbooks/ai-engineering/ai-engineering-handbook-v3.3.html',
  agent:'handbooks/agent-engineering/agent-engineering-master-manual-v2.9.html',
  fde:'handbooks/fde/fde-handbook-v1.6.html',
  saa:'handbooks/aws-saa-c03/saa-c03-visual-handbook-2026.09.html',
  aiarch:'handbooks/ai-architecture/ai-architects-handbook-v1.3.html',
  evals:'handbooks/ai-evaluation/ai-evaluation-field-guide-2026.html',
  pmprod:'handbooks/project-product/project-product-field-guide-v1.html',
};
(async()=>{
  await fs.mkdir(output,{recursive:true});
  const browser=await chromium.launch(process.env.CHROMIUM_EXECUTABLE?{executablePath:process.env.CHROMIUM_EXECUTABLE,args:['--no-sandbox']}:{});
  try {
    for(const [name,file] of Object.entries(files)) {
      const context=await browser.newContext({viewport:{width:1440,height:1000}});
      const page=await context.newPage();const errors=[];
      const redrawHybrid=page.locator('[id="41f-hybrid"]');
      page.on('pageerror',error=>errors.push(error.message));
      await page.goto(pathToFileURL(path.join(root,file)).href);
      // Learning lens: the first step-through diagram walks forward, wraps backwards and resets.
      if(await page.locator('.lens-visual[data-steps]').count()) {
        const r=await page.evaluate(()=>{const f=document.querySelector('.lens-visual[data-steps]');const c=f.querySelector('.lens-controls');const n=Number(f.dataset.steps);const svg=f.querySelector('svg');
          c.querySelector('[data-lens-act="next"]').click();const first=c.querySelector('.lens-status').textContent,stepping=svg.classList.contains('stepping'),lit=f.querySelectorAll('.lens-steps li.on').length,edges=svg.querySelectorAll('.lens-edge.on').length;
          c.querySelector('[data-lens-act="prev"]').click();const wrapped=c.querySelector('.lens-status').textContent;
          c.querySelector('[data-lens-act="all"]').click();return {hidden:c.hidden,n,first,stepping,lit,edges,wrapped,reset:svg.classList.contains('stepping')};});
        assert.equal(r.hidden,false,`${name}: lens controls stayed hidden`);
        assert.match(r.first,/^Step 1 of /);assert.equal(r.stepping,true);assert.equal(r.lit,1);assert.ok(r.edges>=1,`${name}: step 1 highlights no arrow`);
        assert.match(r.wrapped,new RegExp(`^Step ${r.n} of `));assert.equal(r.reset,false);
      }
      if(name==='system') {
        await page.locator('#coreToggle').click();
        assert.equal(await page.evaluate(()=>document.body.classList.contains('core-only')),true);
        assert.equal(await page.locator('#coreToggle').getAttribute('aria-pressed'),'true');
        await page.locator('#coreToggle').click();
        assert.equal(await page.evaluate(()=>document.body.classList.contains('core-only')),false);
      }
      if(name==='saa') {
        assert.equal(await page.locator('.redraw-card').count(),8);
        await page.locator('label[for="filter-handbook"]').click();
        assert.equal(await redrawHybrid.isVisible(),true);
        await page.locator('label[for="filter-domain-1"]').click();
        assert.equal(await page.locator('#filter-domain-1').isChecked(),true);
        assert.equal(await page.locator('#september-revision').isVisible(),false);
        assert.equal(await redrawHybrid.isVisible(),false);
        await page.locator('label[for="filter-all"]').click();
        assert.equal(await page.locator('#filter-all').isChecked(),true);
        await redrawHybrid.locator('summary').click();
        assert.equal(await redrawHybrid.locator('.redraw-figure').isVisible(),true);
        assert.equal(await redrawHybrid.locator('.redraw-questions dt').count(),4);
        await page.locator('#practice-q01 summary').click();
        assert.equal(await page.locator('#practice-q01 .answer').isVisible(),true);
        await page.locator('#practice-q01 button[data-confidence="green"]').click();
        assert.equal(await page.locator('#practice-q01').getAttribute('data-confidence'),'green');
        await page.locator('#themeBtn').click();
        assert.equal(await page.locator('html').getAttribute('data-theme'),'dark');
      }
      if(['system','interview','saa'].includes(name))await page.locator('#search').fill('zz-no-results-zz');
      await page.emulateMedia({media:'print'});
      if(name!=='saa') await page.evaluate(()=>window.dispatchEvent(new Event('beforeprint')));
      assert.equal(await page.evaluate(()=>[...document.querySelectorAll('details.lens-model,details.lens-sketch')].every(d=>d.open)),true,`${name}: print hides a model answer or sketch`);
      if(name==='saa') {
        await page.evaluate(()=>window.dispatchEvent(new Event('beforeprint')));
        assert.equal(await page.locator('[id="41h-dr"] details').getAttribute('open'),'');
      }
      const selector={system:'.chapter',interview:'.resource-card',ai:'.scenario-content',saa:'.chapter,.topic-card',pmprod:'.panel,.grid > .card'}[name];
      if(selector)assert.equal(await page.locator(selector).evaluateAll(nodes=>nodes.every(n=>getComputedStyle(n).display!=='none')),true,`${name}: print omitted filtered or inactive content`);
      await page.pdf({path:path.join(output,`${name}-print.pdf`),format:'A4'});
      await page.emulateMedia({media:'screen'});
      if(['system','interview','saa'].includes(name))await page.locator('#search').fill('');
      await page.screenshot({path:path.join(output,`${name}-desktop.png`),animations:'disabled'});
      await page.setViewportSize({width:390,height:844});
      assert.ok(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth+1),`${name}: page scrolls sideways at 390 px`);
      await page.screenshot({path:path.join(output,`${name}-mobile.png`),animations:'disabled'});
      if(name==='saa') {
        if(!await redrawHybrid.locator('details').evaluate(el=>el.open))
          await redrawHybrid.locator('summary').click();
        await redrawHybrid.screenshot({path:path.join(output,'saa-hybrid-redraw-mobile.png'),animations:'disabled'});
        assert.equal(await redrawHybrid.evaluate(el=>el.scrollWidth<=el.clientWidth+1),true,'SAA redraw card overflowed the mobile page');
      }
      assert.deepEqual(errors,[],`${name}: uncaught page error`);
      await context.close();
    }
    for(const name of ['system','interview']) {
      const context=await browser.newContext({acceptDownloads:true});
      await context.addInitScript(()=>Object.defineProperty(window,'localStorage',{get(){throw new DOMException('Blocked','SecurityError');}}));
      const page=await context.newPage();const errors=[];
      page.on('pageerror',error=>errors.push(error.message));
      page.on('dialog',dialog=>dialog.accept());
      await page.goto(pathToFileURL(path.join(root,files[name])).href);
      if(name==='system')await page.locator('.done').first().check();
      else {
        // Users click the wrapping label; the decorative check overlays the input.
        await page.locator('.check-wrap').first().click();
        assert.equal(await page.locator('.resource-checkbox').first().isChecked(),true);
      }
      assert.match(await page.locator(name==='system'?'#ptxt':'#progressText').textContent(),/^1 \//);
      assert.match(await page.locator('#storageStatus').textContent(),/tab only/);
      if(name==='interview') {
        await page.locator('.feynman-notes').first().fill('Synthetic memory-only evidence');
        const download=page.waitForEvent('download');await page.locator('#exportNotes').click();
        const target=path.join(output,'interview-synthetic-backup.json');await(await download).saveAs(target);
        const backup=JSON.parse(await fs.readFile(target,'utf8'));
        assert.equal(backup.notes.python,'Synthetic memory-only evidence');
        await page.locator('#reset').click();
        assert.match(await page.locator('#progressText').textContent(),/^0 \//);
        assert.equal(await page.locator('.feynman-notes').first().inputValue(),'Synthetic memory-only evidence');
      }
      await page.locator('#search').fill('zz-no-results-zz');
      assert.deepEqual(errors,[]);
      await context.close();
    }
    console.log('Handbook browser smoke passed: filtered print, inactive AI scenarios, storage fallback, note export and reset, learning-lens steppers, core path, print answers and 390 px overflow.');
  } finally {await browser.close();}
})().catch(error=>{console.error(error);process.exitCode=1;});
