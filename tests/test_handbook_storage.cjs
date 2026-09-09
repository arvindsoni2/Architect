// Execute the actual standalone-page scripts against a DOM. Chromium also checks layout in CI.
const {test} = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');
const {parseHTML} = require('linkedom');
const root = path.join(__dirname, '..');
const system = 'handbooks/system-design/system-design-concept-handbook-v5.html';
const interview = 'learning-paths/ai-ml-interview/interview-resource-accelerator-v4.3.html';

function page(file, storage) {
  const source = fs.readFileSync(path.join(root, file), 'utf8');
  const {document, window} = parseHTML(source);
  const context = {document, window, location:{hash:''}, history:{replaceState(){}}, confirm:()=>true,
    Blob, URL, console, setTimeout, clearTimeout};
  Object.defineProperty(context, 'localStorage', {get:()=>storage()});
  vm.createContext(context);
  for(const script of document.querySelectorAll('script:not([src])')) vm.runInContext(script.textContent, context);
  return {document, event:(node,type)=>node.dispatchEvent(new window.Event(type))};
}
const denied = ()=>{throw new Error('Storage denied');};
function memory(seed={}) {
  const values = new Map(Object.entries(seed));
  return {getItem:k=>values.get(k)??null, setItem:(k,v)=>values.set(k,v), removeItem:k=>values.delete(k)};
}

test('system design search and progress work with blocked storage',()=>{
  const {document:d,event} = page(system,denied);
  const box=d.querySelector('.done');box.checked=true;event(box,'change');
  assert.match(d.getElementById('ptxt').textContent,/1 \/ 18/);
  const search=d.getElementById('search');search.value='zz-no-match-zz';event(search,'input');
  assert.equal(d.querySelectorAll('.chapter:not(.hidden)').length,0);
  assert.match(d.getElementById('storageStatus').textContent,/tab only/i);
});

test('interview progress, notes and reset survive blocked storage',()=>{
  const {document:d,event} = page(interview,denied);
  const box=d.querySelector('.resource-checkbox');box.checked=true;event(box,'change');
  assert.match(d.getElementById('progressText').textContent,/^1 \//);
  assert.ok(box.closest('.resource-card').classList.contains('completed'));
  const note=d.querySelector('.feynman-notes');note.value='Synthetic unsaved note';event(note,'input');
  assert.match(d.getElementById('storageStatus').textContent,/tab only/i);
  event(d.getElementById('reset'),'click');
  assert.equal(box.checked,false);
  assert.equal(note.value,'Synthetic unsaved note');
});

test('interview ignores valid JSON with invalid state shapes and field types',()=>{
  for(const bad of ['null','[]','"text"','42','{"v2-python-1":"false","python":17}']) {
    const store=memory({'aiml-interview-resource-progress-v4':bad,'aiml-interview-feynman-notes-v4':bad});
    const {document:d}=page(interview,()=>store);
    assert.match(d.getElementById('progressText').textContent,/^0 \//);
    assert.equal(d.querySelector('.feynman-notes').value,'');
  }
});

test('a later successful progress write does not hide a failed note save',()=>{
  const store=memory(); const original=store.setItem;
  store.setItem=(k,v)=>{if(k.includes('notes'))throw new Error('Quota exceeded');original(k,v);};
  const {document:d,event}=page(interview,()=>store);
  const note=d.querySelector('.feynman-notes');note.value='Keep this note';event(note,'input');
  const box=d.querySelector('.resource-checkbox');box.checked=true;event(box,'change');
  assert.match(d.getElementById('storageStatus').textContent,/tab only/i);
  store.setItem=original;note.value='Recovered note';event(note,'input');
  assert.equal(JSON.parse(store.getItem('aiml-interview-feynman-notes-v4'))[note.dataset.note],'Recovered note');
  assert.doesNotMatch(d.getElementById('storageStatus').textContent,/tab only/i);
});
