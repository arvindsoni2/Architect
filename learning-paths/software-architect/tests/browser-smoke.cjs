// Run with Playwright installed; CI supplies a pinned browser and captures review images.
const {chromium} = require('playwright');
const assert = require('node:assert/strict');
const fs = require('node:fs/promises');
const path = require('node:path');
const {pathToFileURL} = require('node:url');
const output = process.env.ARCHITECT_SCREENSHOTS || '/tmp/architect-browser-review';
const url = pathToFileURL(path.join(__dirname,'../software-architect-grooming-programme-v5.html')).href;

(async()=>{
  await fs.mkdir(output,{recursive:true});
  const browser = await chromium.launch({headless:true});
  try {
    const context = await browser.newContext({viewport:{width:1440,height:1000},acceptDownloads:true});
    const page = await context.newPage();
    const errors=[];
    page.on('pageerror',error=>errors.push(error.message));
    page.on('dialog',dialog=>dialog.accept());
    // Existing learner notes must survive the revised page initialisation.
    await page.addInitScript(()=>localStorage.setItem('arch-v5-note-day1-workspace','Existing synthetic learner note'));
    await page.goto(url);
    assert.equal(await page.locator('[data-note="day1-workspace"]').inputValue(),'Existing synthetic learner note');
    const targets=await page.locator('.nav-link').evaluateAll(nodes=>nodes.map(node=>node.dataset.target));
    for(const target of targets) {
      await page.locator(`[data-target="${target}"]`).click();
      assert.equal(await page.locator('.page-section.active').getAttribute('id'),target);
      assert.ok(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth+1),'Unexpected desktop page overflow');
      if(target.startsWith('day')) {
        await page.locator(`#${target} .visual-panel`).screenshot({animations:'disabled',path:path.join(output,`${target}-diagram.png`)});
      } else if(['overview','pathways','assessment'].includes(target)) {
        await page.screenshot({animations:'disabled',path:path.join(output,`${target}-desktop.png`),fullPage:true});
      }
    }
    await page.locator('[data-target="day3"]').click();
    await page.locator('[data-target="day4"]').click();
    await page.goBack();
    await page.waitForFunction(()=>document.querySelector('.page-section.active').id==='day3');
    await page.evaluate(()=>location.hash='not-a-section');
    await page.waitForFunction(()=>document.querySelector('.page-section.active').id==='overview');
    const badMarkers=await page.evaluate(()=>[...document.querySelectorAll('.arrow')].filter(node=>{
      const marker=getComputedStyle(node).markerEnd.match(/#([^)"]+)/)?.[1];
      return !marker||!document.getElementById(marker);
    }).length);
    assert.equal(badMarkers,0,'An arrowhead reference is unresolved');

    await page.locator('[data-target="pathways"]').click();
    await page.locator('#roleSelect').selectOption('delivery');
    assert.equal(await page.locator('[data-diagnostic="B3"]').inputValue(),'unknown');
    assert.equal(await page.locator('#B3 [data-progress]').isDisabled(),false);
    for(let i=1;i<=6;i++)await page.locator(`[data-diagnostic="B${i}"]`).selectOption('demonstrated');
    await page.evaluate(()=>document.querySelectorAll('[id^="day"] [data-progress]').forEach(input=>{input.checked=true;input.dispatchEvent(new Event('change'));}));
    assert.ok(parseInt(await page.locator('#progressText').textContent())<100,'Capstone must affect completion');
    await page.locator('[data-target="assessment"]').click();
    for(const [i,score] of [15,15,20,15,0,10,10].entries())await page.locator(`[data-score="${i}"]`).fill(String(score));
    for(const gate of ['integrity','evidence','safety'])await page.locator(`[data-gate="${gate}"]`).check();
    assert.equal(await page.locator('[data-progress="assessment-pass"]').isChecked(),false);
    await page.locator('[data-score="4"]').fill('15');
    assert.equal(await page.locator('[data-progress="assessment-pass"]').isChecked(),true);
    await page.evaluate(()=>document.querySelectorAll('#capstone [data-progress]').forEach(input=>{input.checked=true;input.dispatchEvent(new Event('change'));}));
    assert.equal(await page.locator('#progressText').textContent(),'100%');

    await page.locator('[data-target="overview"]').click();
    const download=page.waitForEvent('download');await page.locator('#exportBtn').click();
    const backupPath=path.join(output,'synthetic-backup.json');await (await download).saveAs(backupPath);
    const exported=JSON.parse(await fs.readFile(backupPath,'utf8'));
    assert.equal(exported.data['arch-v5-note-day1-workspace'],'Existing synthetic learner note');
    await page.locator('#importFile').setInputFiles({name:'bad.json',mimeType:'application/json',buffer:Buffer.from(JSON.stringify({...exported,data:{'unrelated-key':'x'}}))});
    await page.waitForFunction(()=>document.getElementById('backupStatus').textContent.startsWith('Import rejected'));
    assert.equal(await page.locator('#progressText').textContent(),'100%');
    const restored={...exported,data:{...exported.data,'arch-v5-note-day1-workspace':'<script>literal imported note</script>'}};
    await page.locator('#importFile').setInputFiles({name:'valid.json',mimeType:'application/json',buffer:Buffer.from(JSON.stringify(restored))});
    await page.waitForFunction(()=>document.getElementById('backupStatus').textContent.startsWith('Backup imported'));
    assert.equal(await page.locator('[data-note="day1-workspace"]').inputValue(),'<script>literal imported note</script>');
    await page.locator('#resetBtn').click();
    assert.equal(await page.locator('[data-note="day1-workspace"]').inputValue(),'');
    assert.equal(await page.locator('#progressText').textContent(),'0%');
    await page.locator('#themeBtn').click();
    await page.screenshot({animations:'disabled',path:path.join(output,'overview-dark.png'),fullPage:true});
    await page.locator('#themeBtn').click();
    await page.setViewportSize({width:390,height:844});
    for(const target of ['pathways','day3','assessment']) {
      await page.locator('#mobileMenu').click();
      await page.locator(`[data-target="${target}"]`).click();
      assert.ok(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth+1),'Unexpected mobile page overflow');
      await page.screenshot({animations:'disabled',path:path.join(output,`${target}-mobile.png`),fullPage:true});
    }
    await page.emulateMedia({media:'print'});
    const printed=await page.locator('.page-section').evaluateAll(nodes=>nodes.every(node=>getComputedStyle(node).display!=='none'));
    assert.equal(printed,true,'Print must include all units');
    await page.pdf({path:path.join(output,'programme-print.pdf'),format:'A4',printBackground:true});
    assert.deepEqual(errors,[]);

    // The real UI must still work when storage is blocked, including reset/export.
    const blocked=await browser.newContext();
    await blocked.addInitScript(()=>Object.defineProperty(window,'localStorage',{get(){throw new DOMException('Blocked','SecurityError');}}));
    const fallback=await blocked.newPage();
    const fallbackErrors=[];fallback.on('pageerror',error=>fallbackErrors.push(error.message));
    fallback.on('dialog',dialog=>dialog.accept());
    await fallback.goto(url);
    assert.match(await fallback.locator('#saveStatus').textContent(),/tab only/);
    await fallback.locator('[data-target="day1"]').click();
    await fallback.locator('[data-note="day1-workspace"]').fill('Memory-only note');
    await fallback.locator('[data-target="overview"]').click();
    const memoryDownload=fallback.waitForEvent('download');await fallback.locator('#exportBtn').click();await memoryDownload;
    await fallback.locator('#resetBtn').click();
    assert.equal(await fallback.locator('[data-note="day1-workspace"]').inputValue(),'');
    assert.deepEqual(fallbackErrors,[]);
    console.log('Browser smoke passed: navigation/history, progress/gates, backup roundtrip, storage fallback, desktop/mobile/print.');
  } finally { await browser.close(); }
})().catch(error=>{console.error(error);process.exitCode=1;});
