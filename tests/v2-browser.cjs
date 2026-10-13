const http=require('node:http'), fs=require('node:fs'), path=require('node:path');
const {chromium}=require('playwright');const assert=require('node:assert/strict');
const root=path.resolve(__dirname,'..');
const server=http.createServer((req,res)=>{let file;try{file=path.resolve(root,'.'+decodeURIComponent(new URL(req.url,'http://localhost').pathname));}catch{res.writeHead(400);return res.end();}if(!file.startsWith(root+path.sep)&&file!==root){res.writeHead(403);return res.end();}if(fs.existsSync(file)&&fs.statSync(file).isDirectory())file=path.join(file,'index.html');if(!fs.existsSync(file)){res.writeHead(404);return res.end();}res.setHeader('Content-Type',({'.html':'text/html; charset=utf-8','.js':'application/javascript; charset=utf-8','.css':'text/css; charset=utf-8'})[path.extname(file)]||'application/octet-stream');fs.createReadStream(file).pipe(res);});
(async()=>{let browser;try{await new Promise(resolve=>server.listen(0,'127.0.0.1',resolve));browser=await chromium.launch();const context=await browser.newContext({viewport:{width:1440,height:1080},reducedMotion:'reduce'});const p=await context.newPage();p.setDefaultTimeout(15000);const errors=[];p.on('pageerror',e=>errors.push(e.message));

await p.goto('http://127.0.0.1:'+server.address().port+'/',{waitUntil:'domcontentloaded'});

   await p.locator('#search').fill('India');assert.equal(await p.locator('#rows tr').count(),1);assert.match(await p.locator('#rows').innerText(),/India/);
   await p.locator('#metric').selectOption('growth');await p.locator('#search').fill('Germany');assert.match(await p.locator('#ranking').innerText(),/-0.27/);
   await p.locator('#reset').click();assert.equal(await p.locator('#rows tr').count(),181);
   const dl=p.waitForEvent('download');await p.locator('#download').click();assert.equal((await dl).suggestedFilename(),'gdp-2023-filtered.csv');
   await p.locator('#clearCompare').click();await p.locator('input[data-country="India"]').check();assert.match(await p.locator('#comparison').innerText(),/India/);
   await p.locator('#rate').fill('0');assert.match(await p.locator('#scenarioText').innerText(),/0\/100/);

await p.locator('#clearCompare').click();await p.reload();assert.equal(await p.locator('#selection button').count(),0);assert.match(await p.locator('#comparison').innerText(),/Select countries/);
await p.evaluate(()=>{history.replaceState=()=>{throw Error('rate limited');};navigator.clipboard.writeText=async text=>{window.copiedView=text;};});await p.locator('#search').fill('India');await p.locator('#share').click();assert.equal(new URL(await p.evaluate(()=>window.copiedView)).searchParams.get('q'),'India');

assert.deepEqual(errors,[],'Unexpected page errors');await p.setViewportSize({width:390,height:844});await p.waitForTimeout(200);assert.equal(await p.evaluate(()=>document.documentElement.scrollWidth>innerWidth+2),false,'Mobile horizontal overflow');console.log('V2 workflow, exports, reload behavior and mobile checks passed.');
}finally{if(browser)await browser.close();await new Promise(resolve=>server.close(resolve));}})().catch(e=>{console.error(e);process.exitCode=1;});
