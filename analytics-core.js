(function(root){
'use strict';
const finite=v=>typeof v==='number'&&Number.isFinite(v);
const mean=a=>{const v=a.filter(finite);return v.length?v.reduce((s,n)=>s+n,0)/v.length:null;};
const median=a=>{const v=a.filter(finite).slice().sort((x,y)=>x-y), n=v.length;return n?(v[Math.floor((n-1)/2)]+v[Math.floor(n/2)])/2:null;};
const csv=rows=>rows.map(row=>row.map(v=>'"'+String(v??'').replace(/^[=+@\t\r]/,'\'$&').replace(/"/g,'""')+'"').join(',')).join('\r\n');
const category=v=>!finite(v)?'Missing':v<=50?'Good':v<=100?'Satisfactory':v<=200?'Moderate':v<=300?'Poor':v<=400?'Very poor':'Severe';
const rolling=(rows,key,n)=>rows.map((r,i)=>mean(rows.slice(Math.max(0,i-n+1),i+1).map(x=>x[key])));
const groupMean=(rows,group,key)=>{const groups={};rows.forEach(r=>(groups[group(r)]??=[]).push(r[key]));return Object.entries(groups).sort(([a],[b])=>a.localeCompare(b)).map(([label,v])=>({label,value:mean(v),count:v.filter(finite).length}));};
const scenario=(base,rate,years)=>finite(base)&&finite(rate)&&Number.isInteger(years)&&years>=0&&years<=30&&rate>=-100&&rate<=100?base*Math.pow(1+rate/100,years):null;
const rank=(rows,key,query='',ascending=false)=>rows.filter(r=>r.country.toLowerCase().includes(query.toLowerCase())&&finite(r[key])).slice().sort((a,b)=>(ascending?1:-1)*(a[key]-b[key])||a.country.localeCompare(b.country));
const range=(rows,start,end)=>rows.filter(r=>(!start||r.date>=start)&&(!end||r.date<=end));
const api={finite,mean,median,csv,category,rolling,groupMean,scenario,rank,range};
if(typeof module!=='undefined')module.exports=api;else root.Analytics=api;
})(typeof window==='undefined'?globalThis:window);
