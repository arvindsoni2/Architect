// Run with Playwright installed; optionally set INTERVIEW_CHROMIUM_EXECUTABLE.
const {chromium}=require('playwright');
const path=require('node:path').resolve(__dirname,'../interview-prep/handbook.html');
(async()=>{
 const browser=await chromium.launch({headless:true,executablePath:process.env.INTERVIEW_CHROMIUM_EXECUTABLE||undefined,args:['--no-sandbox','--disable-dev-shm-usage','--disable-gpu']});
 const page=await browser.newPage({viewport:{width:1440,height:1080}});const errors=[];page.on('pageerror',e=>errors.push(e.message));
 await page.goto('file://'+path);
 const missing=await page.evaluate(()=>[...document.querySelectorAll('a[href^="#"]')].filter(a=>!document.getElementById(a.hash.slice(1))).map(a=>a.hash));
 if(missing.length)throw Error('Missing anchor targets: '+missing.join(','));
 for(const route of ['start','methods','evidence','delivery-lead','agile-delivery-lead','product-owner','product-manager','senior-project-manager','accenture']){
  await page.locator('nav a[href="#'+route+'"]').click();
  await page.locator('#'+route).waitFor({state:'visible'});
  const top=await page.locator('#'+route+' h1').boundingBox();if(top.y<0)throw Error('Route heading clipped: '+route);
  if(await page.locator('.panel:visible').count()!==1||!await page.locator('#'+route).isVisible())throw Error('Route failed: '+route);
 }
 await page.locator('nav a[href="#product-owner"]').click();await page.locator('#product-owner').waitFor({state:'visible'});
 await page.locator('#product-owner a[href="#evidence--s3-smart-timesheet"]').first().click();
 await page.locator('#evidence--s3-smart-timesheet').waitFor({state:'visible'});
 if(!await page.locator('#evidence--s3-smart-timesheet').isVisible())throw Error('Cross-guide link failed');
 await page.locator('#theme').click();if(await page.locator('#theme').getAttribute('aria-pressed')!=='true')throw Error('Theme failed');

 await page.locator('#theme').click();await page.setViewportSize({width:390,height:844});await page.locator('nav a[href="#accenture"]').click();await page.locator('#accenture').waitFor({state:'visible'});
 const overflow=await page.evaluate(()=>document.documentElement.scrollWidth>innerWidth);
 if(overflow)throw Error('Mobile page overflow');
 await page.emulateMedia({media:'print'});if(await page.locator('.panel:visible').count()!==9)throw Error('Print hides guides');
 const plain=await browser.newPage({javaScriptEnabled:false});await plain.goto('file://'+path);if(await plain.locator('.panel:visible').count()!==9)throw Error('No-JS content missing');
 if(errors.length)throw Error(errors.join(','));console.log('Browser QA passed: 9 routes, all anchors, cross-guide links, themes, mobile overflow, print and no-JS content.');
 await browser.close();
})().catch(e=>{console.error(e);process.exit(1);});
