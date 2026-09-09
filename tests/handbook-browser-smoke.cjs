// Real browser coverage for the standalone handbook audit regressions.
const {chromium} = require('playwright');
const assert = require('node:assert/strict');
const fs = require('node:fs/promises');
const path = require('node:path');
const {pathToFileURL} = require('node:url');
const root = path.join(__dirname,'..');
const output = process.env.ARCHITECT_SCREENSHOTS || '/tmp/architect-browser-review';
const files = {
  system:'handbooks/system-design/system-design-concept-handbook-v5.html',
  interview:'learning-paths/ai-ml-interview/interview-resource-accelerator-v4.3.html',
  ai:'handbooks/ai-engineering/ai-engineering-handbook-v3.0.html',
  agent:'handbooks/agent-engineering/agent-engineering-master-manual-v2.7.html',
  fde:'handbooks/fde/fde-handbook-v1.3.html',
};
(async()=>{
  await fs.mkdir(output,{recursive:true});
  const browser=await chromium.launch();
  try {
    for(const [name,file] of Object.entries(files)) {
      const context=await browser.newContext({viewport:{width:1440,height:1000}});
      const page=await context.newPage();const errors=[];
      page.on('pageerror',error=>errors.push(error.message));
      await page.goto(pathToFileURL(path.join(root,file)).href);
      if(['system','interview'].includes(name))await page.locator('#search').fill('zz-no-results-zz');
      await page.emulateMedia({media:'print'});
      const selector={system:'.chapter',interview:'.resource-card',ai:'.scenario-content'}[name];
      if(selector)assert.equal(await page.locator(selector).evaluateAll(nodes=>nodes.every(n=>getComputedStyle(n).display!=='none')),true,`${name}: print omitted filtered or inactive content`);
      await page.pdf({path:path.join(output,`${name}-print.pdf`),format:'A4'});
      await page.emulateMedia({media:'screen'});
      if(['system','interview'].includes(name))await page.locator('#search').fill('');
      await page.screenshot({path:path.join(output,`${name}-desktop.png`),animations:'disabled'});
      await page.setViewportSize({width:390,height:844});
      await page.screenshot({path:path.join(output,`${name}-mobile.png`),animations:'disabled'});
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
    console.log('Handbook browser smoke passed: filtered print, inactive AI scenarios, storage fallback, note export and reset.');
  } finally {await browser.close();}
})().catch(error=>{console.error(error);process.exitCode=1;});
