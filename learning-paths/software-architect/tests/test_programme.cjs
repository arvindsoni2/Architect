const { test } = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');
const html = fs.readFileSync(path.join(__dirname, '../software-architect-grooming-programme-v5.html'), 'utf8');
const source = html.match(/<script id="programme-model">([\s\S]*?)<\/script>/)?.[1] || '';
const context = vm.createContext({TextEncoder});
vm.runInContext(source, context);
const model = context.Programme;

test('missing critical competence cannot be offset by a high total', () => {
  assert.ok(model, 'Programme assessment model is missing');
  for (const scores of [[15,15,20,0,15,10,10], [15,15,20,15,0,10,10]]) {
    assert.equal(model.assess(scores, true, true, true).passed, false);
  }
  assert.equal(model.assess([15,15,20,15,15,10,10], false, true, true).passed, false);
  assert.equal(model.assess([15,15,20,15,15,10,10], true, false, true).passed, false);
  assert.equal(model.assess([15,15,20,15,15,10,10], true, true, false).passed, false);
  assert.equal(model.assess([12,12,16,12,12,8,8], true, true, true).passed, true);
  assert.throws(() => model.assess([16,15,20,15,15,10,10], true, true, true));
});

test('all six bridges are diagnosed and unknown competence stays required', () => {
  assert.ok(model, 'Programme diagnostic model is missing');
  assert.equal(model.requiredBridges({}).length, 6);
  assert.deepEqual(Array.from(model.requiredBridges({B1:'demonstrated',B2:'demonstrated',B3:'practice',B4:'demonstrated',B5:'demonstrated',B6:'demonstrated'})), ['B3']);
});

test('completion includes capstone and assessment but excludes demonstrated bridges', () => {
  assert.ok(model, 'Programme progress model is missing');
  const items = [{id:'b1',bridge:'B1'},{id:'core'},{id:'capstone-evidence'},{id:'assessment-review'}];
  assert.equal(model.progress(items,{core:true,'capstone-evidence':true,'assessment-review':true},{B1:'demonstrated'}),100);
  assert.equal(model.progress(items,{b1:true,core:true},{B1:'practice'}),50);
  assert.equal(model.progress(items,{core:true},{B1:'demonstrated'}),33);
});

test('backup roundtrip preserves notes without accepting unknown or malformed state', () => {
  assert.ok(model, 'Programme backup validation is missing');
  const keys=['arch-v5-note-day1-workspace','arch-v5-day1-step-1','arch-v5-role','arch-v5-diagnostic-B3'];
  const backup={format:'architect-programme',version:1,savedAt:'2026-09-08T12:00:00Z',data:{'arch-v5-note-day1-workspace':'<script>plain learner text</script>','arch-v5-day1-step-1':'1','arch-v5-role':'delivery','arch-v5-diagnostic-B3':'practice'}};
  assert.equal(model.validateBackup(JSON.stringify(backup),keys).data['arch-v5-note-day1-workspace'],backup.data['arch-v5-note-day1-workspace']);
  for(const bad of [{...backup,version:2},{...backup,data:{unrelated:'x'}},{...backup,data:{'arch-v5-role':'bogus'}},{...backup,data:{'arch-v5-day1-step-1':'yes'}},{...backup,data:{'arch-v5-note-day1-workspace':{html:'x'}}},{...backup,data:{'arch-v5-diagnostic-B3':'skip'}}]) {
    assert.throws(()=>model.validateBackup(JSON.stringify(bad),keys));
  }
  assert.throws(()=>model.validateBackup('{',keys));
});

test('all supported notes and historical long notes survive a multibyte backup roundtrip', () => {
  const keys=Array.from({length:28},(_,i)=>'arch-v5-note-example-'+i);
  const data=Object.fromEntries(keys.map(key=>[key,'界'.repeat(100000)]));
  data[keys[0]]='historical note '.repeat(10000);
  const text=JSON.stringify({format:'architect-programme',version:1,data});
  assert.equal(model.validateBackup(text,keys).data[keys[0]],data[keys[0]]);
  assert.ok(model.backupText,'Export serialization and validation are missing');
  assert.equal(model.validateBackup(model.backupText(data,keys,'2026-09-08T12:00:00Z'),keys).data[keys[1]],data[keys[1]]);
  assert.throws(()=>model.backupText({[keys[0]]:'界'.repeat(9000000)},keys,'2026-09-08T12:00:00Z'));
});

test('quota failure still permits durable reset and later writes', () => {
  assert.ok(model.createStore,'Storage recovery implementation is missing');
  const durable=new Map([['arch-v5-note-day1-workspace','old note'],['other-app','keep']]);
  let full=true;
  const storage={get length(){return durable.size;},key:i=>[...durable.keys()][i],getItem:key=>durable.get(key)??null,setItem:(key,value)=>{if(full)throw new Error('QuotaExceededError');durable.set(key,value);},removeItem:key=>durable.delete(key)};
  const states=[];
  const store=model.createStore(storage,saved=>states.push(saved));
  store.setItem('arch-v5-note-day1-workspace','unsaved note');
  assert.equal(store.getItem('arch-v5-note-day1-workspace'),'unsaved note');
  assert.equal(states.at(-1),false);
  store.removeItem('arch-v5-note-day1-workspace');
  assert.equal(durable.has('arch-v5-note-day1-workspace'),false);
  assert.equal(model.createStore(storage,()=>{}).getItem('arch-v5-note-day1-workspace'),null);
  assert.equal(durable.get('other-app'),'keep');
  full=false;
  store.setItem('arch-v5-note-day1-workspace','new note');
  assert.equal(durable.get('arch-v5-note-day1-workspace'),'new note');
  assert.equal(states.at(-1),true);
});

test('recovering storage flushes every unsaved note before reporting durable success', () => {
  assert.ok(model.createStore,'Storage recovery implementation is missing');
  const durable=new Map();let full=false;const states=[];
  const storage={get length(){return durable.size;},key:i=>[...durable.keys()][i],getItem:key=>durable.get(key)??null,setItem:(key,value)=>{if(full)throw new Error('QuotaExceededError');durable.set(key,value);},removeItem:key=>durable.delete(key)};
  const store=model.createStore(storage,saved=>states.push(saved));
  full=true;store.setItem('arch-v5-note-a','first');store.setItem('arch-v5-note-b','second');
  assert.equal(states.at(-1),false);
  full=false;store.setItem('arch-v5-theme','dark');
  assert.equal(durable.get('arch-v5-note-a'),'first');assert.equal(durable.get('arch-v5-note-b'),'second');assert.equal(states.at(-1),true);
});

test('shrinking a later note frees quota for an earlier pending larger note', () => {
  const durable=new Map([['arch-v5-note-a','a'.repeat(40)],['arch-v5-note-b','b'.repeat(40)]]);
  const states=[];
  const storage={get length(){return durable.size;},key:i=>[...durable.keys()][i],getItem:key=>durable.get(key)??null,setItem:(key,value)=>{
    const used=[...durable].reduce((sum,[k,v])=>sum+(k===key?0:v.length),0);
    if(used+value.length>100)throw new Error('QuotaExceededError');durable.set(key,value);
  },removeItem:key=>durable.delete(key)};
  const store=model.createStore(storage,saved=>states.push(saved));
  store.setItem('arch-v5-note-a','a'.repeat(70));
  store.setItem('arch-v5-note-b','b'.repeat(10));
  assert.equal(durable.get('arch-v5-note-b').length,10);
  assert.equal(durable.get('arch-v5-note-a').length,70);
  assert.equal(states.at(-1),true);
});
