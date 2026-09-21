// Evaluate only the manual's reviewed data declarations and pure SVG renderer.
const fs = require('node:fs');
const vm = require('node:vm');
const html = fs.readFileSync(process.argv[2], 'utf8');
const script = html.match(/<script>([\s\S]*?)<\/script>/)[1];
new vm.Script(script); // Parse the complete script without running browser code.
const data = script.slice(script.indexOf('const PROGRAMME ='), script.indexOf('/* ============================ engine'));
const renderer = script.slice(script.indexOf('const TYPECOL='), script.indexOf('function codeBlock('));
const progress = script.slice(script.indexOf('const LAB_STATUS'), script.indexOf('function labTrack('));
const result = vm.runInNewContext(data + renderer + progress + `;({PROGRAMME,APPS,svgs:APPS.map(diagramSVG),
invalidExplicitSvg:(()=>{const app=JSON.parse(JSON.stringify(APPS[0])),edge=app.diagram.edges.find(x=>x.l),node=app.diagram.nodes.find(x=>x.id===edge.f);edge.lx=node.x+75;edge.ly=node.y+26;return diagramSVG(app);})(),
themeChecks:typeof normaliseTheme==='function' && typeof nextTheme==='function' ?
 [normaliseTheme('dark'),normaliseTheme('light'),normaliseTheme('unsupported'),nextTheme('light'),nextTheme('dark')] : null,
progressChecks:typeof validateProgress==='function' ? [
 {version:1,labs:{l1:{status:'building',actual:2.5,evidence:{0:true}}}},
 {version:1,labs:{alien:{status:'building'}}},
 {version:1,labs:{l1:{actual:-1}}},
 {version:1,labs:{l1:{status:'made_up'}}},
 {version:1,labs:{l1:{evidence:{0:'yes'}}}}
].map(x=>{try{return {ok:true,value:validateProgress(x)};}catch{return {ok:false};}}):null})`, Object.create(null), {timeout:2000});
process.stdout.write(JSON.stringify(result));
