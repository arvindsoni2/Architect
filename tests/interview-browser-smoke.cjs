// Run with Playwright installed; optionally set INTERVIEW_CHROMIUM_EXECUTABLE.
const {chromium}=require('playwright');
const path=require('node:path').resolve(__dirname,'../interview-prep/handbook.html');
(async()=>{
 const browser=await chromium.launch({headless:true,executablePath:process.env.INTERVIEW_CHROMIUM_EXECUTABLE||undefined,args:['--no-sandbox','--disable-dev-shm-usage','--disable-gpu']});
 const page=await browser.newPage({viewport:{width:1440,height:1080}});const errors=[];page.on('pageerror',e=>errors.push(e.message));
 await page.goto('file://'+path);
 const missing=await page.evaluate(()=>[...document.querySelectorAll('a[href^="#"]')].filter(a=>!document.getElementById(a.hash.slice(1))).map(a=>a.hash));
 if(missing.length)throw Error('Missing anchor targets: '+missing.join(','));
 for(const route of ['start','methods','evidence','connect','decisions','arb','delivery-lead','agile-delivery-lead','product-owner','product-manager','senior-project-manager','software-ai-architect','ai-engineer','forward-deployed-engineer','accenture','accenture-questions','accenture-fde']){
  await page.locator('nav a[href="#'+route+'"]').click();
  await page.locator('#'+route).waitFor({state:'visible'});
  const top=await page.locator('#'+route+' h1').boundingBox();if(top.y<0)throw Error('Route heading clipped: '+route);
  if(await page.locator('.panel:visible').count()!==1||!await page.locator('#'+route).isVisible())throw Error('Route failed: '+route);
 }
 await page.locator('nav a[href="#product-owner"]').click();await page.locator('#product-owner').waitFor({state:'visible'});
 await page.locator('#product-owner a[href="#evidence--s3-smart-timesheet"]').first().click();
 await page.locator('#evidence--s3-smart-timesheet').waitFor({state:'visible'});
 if(!await page.locator('#evidence--s3-smart-timesheet').isVisible())throw Error('Cross-guide link failed');
 await page.locator('nav a[href="#accenture-questions"]').click();await page.locator('#accenture-questions').waitFor({state:'visible'});
 await page.locator('#accenture-questions a[href="#accenture-questions--what-is-api-first-and-whats-your-experience"]').first().click();
 await page.locator('#accenture-questions--what-is-api-first-and-whats-your-experience').waitFor({state:'visible'});
 await page.locator('#accenture-questions a[href="#evidence--s3-smart-timesheet"]').first().click();
 await page.locator('#evidence--s3-smart-timesheet').waitFor({state:'visible'});
 await page.locator('#theme').click();if(await page.locator('#theme').getAttribute('aria-pressed')!=='true')throw Error('Theme failed');

 await page.locator('nav a[href="#accenture-fde"]').click();
 await page.locator('#accenture-fde a[href="#accenture-fde--worked-programme-and-commercial-case"]').first().click();
 await page.locator('#accenture-fde--worked-programme-and-commercial-case').waitFor({state:'visible'});
 await page.locator('#accenture-fde a[href="#evidence--s1-genai-order-automation"]').first().click();
 await page.locator('#evidence--s1-genai-order-automation').waitFor({state:'visible'});

 await page.locator('#theme').click();await page.setViewportSize({width:390,height:844});await page.locator('nav a[href="#accenture-questions"]').click();await page.locator('#accenture-questions').waitFor({state:'visible'});
 const overflow=await page.evaluate(()=>document.documentElement.scrollWidth>innerWidth);
 if(overflow)throw Error('Mobile page overflow');
 await page.locator('nav a[href="#accenture-fde"]').click();await page.locator('#accenture-fde').waitFor({state:'visible'});
 if(await page.evaluate(()=>document.documentElement.scrollWidth>innerWidth))throw Error('FDE mobile page overflow');
 for(const route of ['software-ai-architect','ai-engineer','forward-deployed-engineer']){await page.locator('nav a[href="#'+route+'"]').click();await page.locator('#'+route).waitFor({state:'visible'});if(await page.evaluate(()=>document.documentElement.scrollWidth>innerWidth))throw Error('Mobile page overflow: '+route);}
 await page.emulateMedia({media:'print'});if(await page.locator('.panel:visible').count()!==17)throw Error('Print hides guides');
 const plain=await browser.newPage({javaScriptEnabled:false});await plain.goto('file://'+path);if(await plain.locator('.panel:visible').count()!==17)throw Error('No-JS content missing');
 // Standalone guide pages: one per Markdown source, with practice mode.
 const dir=require('node:path').dirname(path),pages=['index.html','shared/handbook.html','shared/evidence-bank.html','shared/connect-the-dots.html','shared/decision-ledger.html','shared/architecture-review.html','dot-drill.html','roles/delivery-lead.html','roles/agile-delivery-lead.html','roles/product-owner.html','roles/product-manager.html','roles/senior-project-manager.html','roles/software-ai-architect.html','roles/ai-engineer.html','roles/forward-deployed-engineer.html','vacancies/accenture-product-owner.html','vacancies/accenture-product-owner-questions.html','vacancies/accenture-fde.html'];
 const guide=await browser.newPage({viewport:{width:390,height:844}});guide.on('pageerror',e=>errors.push(e.message));
 for(const file of pages){await guide.goto('file://'+dir+'/'+file);
  const gone=await guide.evaluate(()=>[...document.querySelectorAll('a[href^="#"]')].filter(a=>a.hash&&!document.getElementById(decodeURIComponent(a.hash.slice(1)))).map(a=>a.hash));
  if(gone.length)throw Error(file+' missing anchors: '+gone.join(','));
  if(await guide.evaluate(()=>document.documentElement.scrollWidth>innerWidth))throw Error('Guide page overflow: '+file);}
 await guide.setViewportSize({width:1280,height:900});await guide.goto('file://'+dir+'/roles/ai-engineer.html');
 const qa=guide.locator('.qa').first();await guide.locator('#practice').click();
 if(await qa.locator('.qa-body').isVisible())throw Error('Practice mode did not hide the model answer');
 await qa.locator('.reveal-btn').click();if(!await qa.locator('.qa-body').isVisible())throw Error('Reveal did not show the model answer');
 await qa.locator('.qa-tools input').check();await guide.reload();
 if(!(await guide.locator('#practised-count').textContent()).startsWith('1 of'))throw Error('Practised tick not saved');
 await guide.locator('nav a[aria-current="page"]').waitFor();
 await guide.emulateMedia({media:'print'});await guide.goto('file://'+dir+'/roles/product-owner.html');
 if(!await guide.locator('.qa-li .qa-ans').first().isVisible())throw Error('Print hides list answers');
 const blocked=await browser.newContext();await blocked.addInitScript(()=>Object.defineProperty(window,'localStorage',{get(){throw new DOMException('Blocked','SecurityError');}}));
 const bp=await blocked.newPage();bp.on('pageerror',e=>errors.push('blocked storage: '+e.message));await bp.goto('file://'+dir+'/roles/ai-engineer.html');await bp.locator('#practice').click();await bp.locator('.qa-tools input').first().check();
 // Theme must survive moving between guides even when each file has its own storage (Firefox, Safari).
 const isDark=pg=>pg.evaluate(()=>document.documentElement.classList.contains('dark'));
 const tp=await blocked.newPage();await tp.goto('file://'+dir+'/roles/ai-engineer.html');await tp.locator('#theme').click();
 await tp.locator('nav a',{hasText:'Product Owner'}).click();if(!await isDark(tp))throw Error('Dark view lost moving between guide pages');
 await tp.locator('nav a',{hasText:'Tabbed reading view'}).click();if(!await isDark(tp))throw Error('Dark view lost opening the tabbed view');
 await tp.locator('nav a[href="#product-manager"]').click();if(!await isDark(tp))throw Error('Dark view lost switching tabs');
 await tp.locator('#theme').click();await tp.locator('nav a[href="#start"]').click();await tp.locator('#start a[href*="index.html"]').first().click();
 if(await isDark(tp))throw Error('Light view not carried back to guide pages');
 // Dot drill: picking a story and lens writes the question; without scripts the tables remain.
 await guide.emulateMedia({media:'screen'});await guide.goto('file://'+dir+'/dot-drill.html');await guide.locator('#drill').waitFor({state:'visible'});
 await guide.locator('#roles button',{hasText:'Architect'}).click();await guide.locator('.cell[data-s="0"][data-l="1"]').click();
 if(!(await guide.locator('#prompt').textContent()).includes('GenAI orders'))throw Error('Drill prompt did not use the chosen story');
 if(!(await guide.locator('#pair').textContent()).startsWith('Pair it'))throw Error('Drill did not suggest a pairing for a work story in an architect interview');
 await guide.locator('#start').click();if(await guide.locator('#start').textContent()!=='Stop')throw Error('Drill timer did not start');await guide.locator('#start').click();
 const nojs=await browser.newPage({javaScriptEnabled:false});await nojs.goto('file://'+dir+'/dot-drill.html');
 if(await nojs.locator('#drill').isVisible()||!await nojs.locator('#lens-prompts').isVisible())throw Error('Drill no-JS fallback wrong');
 const flat=await browser.newPage({javaScriptEnabled:false});await flat.goto('file://'+dir+'/roles/ai-engineer.html');
 if(!await flat.locator('.qa-body').first().isVisible()||!await flat.locator('#practice').isHidden())throw Error('No-JS guide page incomplete');
 if(errors.length)throw Error(errors.join(','));console.log('Browser QA passed: 17 routes, all anchors, cross-guide links, themes, mobile overflow, print and no-JS content; 18 pages with practice mode and the dot drill; theme carried between pages.');
 await browser.close();
})().catch(e=>{console.error(e);process.exit(1);});
