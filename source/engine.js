(function(){
var D=window.CASE;
var $=function(s,r){return (r||document).querySelector(s)};
var el=function(tag,attrs,html){var e=document.createElement(tag); if(attrs){for(var k in attrs){e.setAttribute(k,attrs[k])}} if(html!==undefined){e.innerHTML=html} return e};
var pct=function(n){return (Math.round(n*10)/10)+'%'};

/* ---------- brief blocks ---------- */
var blocks=$('#blocks');
(D.blocks||[]).forEach(function(b){
  var w=el('div',{'class':'blk'});
  if(b.type==='bars'){
    w.innerHTML='<div class="sec-head"><h3>'+b.title+'</h3>'+(b.note?'<p class="muted">'+b.note+'</p>':'')+'</div>';
    var polls=el('div',{'class':'polls'});
    b.polls.forEach(function(p){
      var d=el('div',{'class':'poll'},'<h3>'+p.q+'</h3>');
      p.rows.forEach(function(r){
        d.appendChild(el('div',{'class':'row'+(r[2]?' win':'')},'<span class="lbl">'+r[0]+'</span><span class="n">'+pct(r[1])+'</span><span class="bar"><i style="width:'+r[1]+'%"></i></span>'));
      });
      polls.appendChild(d);
    });
    w.appendChild(polls);
  } else if(b.type==='cards'){
    w.innerHTML='<div class="sec-head"><h3>'+b.title+'</h3></div><div class="cols3">'+b.items.map(function(x){return '<div class="item"><h3>'+x[0]+'</h3><p class="muted">'+x[1]+'</p></div>'}).join('')+'</div>';
  } else if(b.type==='stake'){
    var q=b.q;
    w.innerHTML='<div class="sec-head"><h3>'+b.title+'</h3><p class="muted">'+b.note+'</p></div><div class="stake" role="group" aria-label="Stakeholder map by power and influence">'
      +'<span class="ax">Power, low to high</span>'
      +q.map(function(x){return '<div class="q'+(x.key?' key':'')+'"><h4>'+x.h+'</h4><div class="names">'+x.names.map(function(n){return '<span>'+n+'</span>'}).join('')+'</div><p>'+x.p+'</p></div>'}).join('')
      +'<span></span><span class="xl">Influence, low to high</span><span class="xl"></span></div>';
  } else if(b.type==='text'){
    w.innerHTML='<p class="muted measure">'+b.text+'</p>';
  } else if(b.type==='img'){
    w.innerHTML='<figure style="margin:0"><img class="wide" src="'+b.src+'" alt="'+b.alt+'" loading="lazy"><figcaption class="cap">'+b.cap+'</figcaption></figure>';
  }
  blocks.appendChild(w);
});

/* ---------- design explorer ---------- */
var tabs=$('#tabs'), panel=$('#panel'), cur=0;
D.des.forEach(function(d,i){
  var b=el('button',{'class':'tab',type:'button',role:'tab',id:'tab'+i,'aria-controls':'panel'},d.k);
  b.addEventListener('click',function(){pick(i,true)});
  b.addEventListener('keydown',function(e){
    var n=null;
    if(e.key==='ArrowRight')n=(cur+1)%D.des.length; else if(e.key==='ArrowLeft')n=(cur+D.des.length-1)%D.des.length;
    if(n!==null){e.preventDefault(); pick(n,true)}
  });
  tabs.appendChild(b);
});
function pick(i,focus){
  cur=i; var d=D.des[i];
  Array.prototype.forEach.call(tabs.children,function(b,j){
    b.setAttribute('aria-selected',j===i?'true':'false'); b.tabIndex=(j===i)?0:-1;
    if(j===i&&focus)b.focus();
  });
  panel.setAttribute('aria-labelledby','tab'+i);
  var ims=d.imgs||[[d.img,d.alt]];var h='<div class="shot">'+ims.map(function(m){return '<img src="'+m[0]+'" alt="'+m[1]+'">'}).join('')+'</div><div class="info">';
  h+='<div class="kv"><span class="mono">What it tried</span><p>'+d.tried+'</p></div>';
  if(d.said) h+='<div class="kv"><span class="mono">'+(d.saidLabel||'What people said')+'</span><p>'+d.said+'</p></div>';
  if(d.took) h+='<div class="took"><span class="mono">Taken forward</span><p><strong>'+d.took+'</strong></p></div>';
  if(d.icons) h+='<div class="tabicons">'+d.icons.map(function(m){return '<img src="'+m[0]+'" alt="'+m[1]+'">'}).join('')+'</div>';
  if(d.recipe){
    h+='<div class="kv"><span class="mono">Where each part came from</span></div><div class="recipe">'+d.recipe.map(function(r){return '<button type="button" data-g="'+r[1]+'"><b>'+r[0]+'</b> '+r[2]+'</button>'}).join('')+'</div>';
  }
  h+='</div>';
  panel.innerHTML=h;
  Array.prototype.forEach.call(panel.querySelectorAll('.recipe button'),function(b){
    b.addEventListener('click',function(){pick(+b.getAttribute('data-g'),true)});
  });
}
pick(D.des.length-1,false);

/* ---------- try it ---------- */
var T=D.tryit, root=$('#try-body');
if(T.type==='challenges'){
  var mode=0, sel=0;
  root.innerHTML='<div class="rack-ui"><div class="seg" role="radiogroup" aria-label="Challenge type" id="cMode"></div><span class="muted" id="cSum"></span></div>'
    +'<div class="chal"><ul class="chal-list" id="cList"></ul><div class="chal-detail" id="cDet" aria-live="polite"></div></div>';
  T.modes.forEach(function(m,i){
    var b=el('button',{'class':'chip',type:'button',role:'radio','aria-checked':i===0?'true':'false'},m.name);
    b.addEventListener('click',function(){mode=i;sel=0;Array.prototype.forEach.call($('#cMode').children,function(x,j){x.setAttribute('aria-checked',j===i?'true':'false')});drawC()});
    $('#cMode').appendChild(b);
  });
  var drawC=function(){
    var m=T.modes[mode];
    $('#cSum').textContent='Money saved so far in this view: '+m.saved;
    $('#cList').innerHTML=m.items.map(function(c,i){return '<li><button type="button" data-i="'+i+'" aria-pressed="'+(i===sel)+'"><span class="nm">'+c[0]+'</span><span class="mono" style="color:var(--ink)">'+c[1]+'%</span><span class="meter"><i style="width:'+c[1]+'%"></i></span></button></li>'}).join('');
    var c=m.items[sel];
    $('#cDet').innerHTML='<span class="mono">'+m.name+' challenge</span><h3>'+c[0]+'</h3><div class="big">'+c[1]+'<small>% done</small></div><div class="meter lg"><i style="width:'+c[1]+'%"></i></div>'+(c[3]?'<p class="cdesc">'+c[3]+'</p>':'')+'<dl class="specs"><dt>Saving range</dt><dd>'+c[2]+'</dd></dl><p class="muted">Figures come from the final screens. Tap another challenge to compare.</p>';
    Array.prototype.forEach.call($('#cList').querySelectorAll('button'),function(b){b.addEventListener('click',function(){sel=+b.getAttribute('data-i');drawC()})});
  };
  drawC();
}
if(T.type==='checkup'){
  var P={check:'M4 12l5 5 11-11',dash:'M5 12h14',drop:'M12 3c3 4 6 7 6 11a6 6 0 0 1-12 0c0-4 3-7 6-11z',x:'M6 6l12 12M18 6L6 18',z:'M6 6h12L6 18h12',wave:'M3 12c2-3 4-3 6 0s4 3 6 0 4-3 6 0',flame:'M12 3c1 4 5 5 5 10a5 5 0 0 1-10 0c0-2 1-3 2-4 0 2 1 2 2 2 0-3-1-5 1-8z'};
  var ic=function(n){return '<svg viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="'+P[n]+'"/></svg>'};
  var st={q1:null,q2:[],q3:null}, entries=[], jc=0;
  root.innerHTML='<div class="seg" role="radiogroup" aria-label="Journal colour theme" id="jSeg"></div>'
    +'<form class="chk" id="chk" autocomplete="off"><p class="mono" id="chkDate"></p>'
    +'<fieldset><legend>1. Today I feel</legend><div class="icons" id="q1"></div></fieldset>'
    +'<fieldset><legend>2. Today, while eating, I</legend><div class="boxes" id="q2"></div></fieldset>'
    +'<fieldset><legend>3. After eating, my body felt</legend><div class="icons" id="q3"></div></fieldset>'
    +'<label class="notes"><span>My notes for today (optional)</span><textarea id="qn" rows="3" placeholder="How you felt today, what you ate, something that gives you strength"></textarea></label>'
    +'<div class="step-nav"><button class="btn" type="submit" id="qs">Save today</button><button class="btn ghost" type="button" id="qr">Clear</button></div>'
    +'<p class="note" id="qmsg" aria-live="polite"></p></form><ol class="entries" id="entries"></ol>';
  $('#chkDate').textContent='Today is '+new Date().toLocaleDateString(undefined,{day:'2-digit',month:'2-digit',year:'numeric'});
  T.journals.forEach(function(j,i){
    var b=el('button',{'class':'chip',type:'button',role:'radio','aria-checked':i===0?'true':'false'},'<span class="sw" style="--c:'+j[1]+'"></span>'+j[0]);
    b.addEventListener('click',function(){jc=i;$('#chk').style.setProperty('--jc',j[1]);Array.prototype.forEach.call($('#jSeg').children,function(x,k){x.setAttribute('aria-checked',k===i?'true':'false')})});
    $('#jSeg').appendChild(b);
  });
  $('#chk').style.setProperty('--jc',T.journals[0][1]);
  var iconRow=function(id,list,key){
    list.forEach(function(it,i){
      var b=el('button',{'class':'ico',type:'button','aria-pressed':'false'},ic(it[1])+'<span>'+it[0]+'</span>');
      b.addEventListener('click',function(){st[key]=(st[key]===it[0])?null:it[0];Array.prototype.forEach.call($(id).children,function(x,j){x.setAttribute('aria-pressed',st[key]===list[j][0]?'true':'false')})});
      $(id).appendChild(b);
    });
  };
  iconRow('#q1',T.q1,'q1'); iconRow('#q3',T.q3,'q3');
  T.q2.forEach(function(t,i){
    var l=el('label',{'class':'cb'},'<input type="checkbox" id="cb'+i+'"><span>'+t+'</span>');
    $('input',l).addEventListener('change',function(){st.q2=T.q2.filter(function(x,j){return $('#cb'+j).checked})});
    $('#q2').appendChild(l);
  });
  $('#qr').addEventListener('click',function(){reset();$('#qmsg').textContent=''});
  function reset(){st={q1:null,q2:[],q3:null};$('#qn').value='';Array.prototype.forEach.call(document.querySelectorAll('#q1 button,#q3 button'),function(b){b.setAttribute('aria-pressed','false')});T.q2.forEach(function(t,i){$('#cb'+i).checked=false})}
  $('#chk').addEventListener('submit',function(e){
    e.preventDefault();
    if(!st.q1&&!st.q3&&!st.q2.length){$('#qmsg').textContent='Pick at least one answer first. Every question is optional, so a single answer is enough.';return}
    entries.push({a:st.q1,b:st.q2.slice(),c:st.q3,n:$('#qn').value});
    $('#qmsg').textContent=T.saved;
    $('#entries').innerHTML=entries.map(function(en,i){return '<li><span class="mono">Entry '+(i+1)+'</span> Felt <b>'+(en.a||'no answer')+'</b>. While eating: '+(en.b.length?en.b.join(', ').toLowerCase():'nothing ticked')+'. Body felt <b>'+(en.c||'no answer')+'</b>.'+(en.n?' Note: '+en.n.replace(/</g,'&lt;'):'')+'</li>'}).join('');
    reset();
  });
}
if(T.type==='measure'){
  var tol=T.tol;
  root.innerHTML='<div class="msr-ctl"><label for="tol" class="mono">Allowed difference: <b id="tolv"></b> mm</label><input type="range" id="tol" min="0" max="6" step="1" value="'+tol+'"><span class="muted" id="msum" aria-live="polite"></span></div><ul class="msr" id="msr"></ul>';
  var drawM=function(){
    tol=+$('#tol').value; $('#tolv').textContent=tol;
    var ok=0;
    $('#msr').innerHTML=T.rows.map(function(r){
      var d=Math.abs(r[1]-r[2]), good=d<=tol; if(good) ok++;
      var mx=Math.max.apply(null,T.rows.map(function(x){return Math.max(x[1],x[2])}));
      return '<li><span class="nm">'+r[0]+'</span><span class="bars"><i class="o" style="width:'+(r[1]/mx*100)+'%"></i><i class="r" style="width:'+(r[2]/mx*100)+'%"></i></span><span class="mono">'+(r[1]/10)+' cm vs '+(r[2]/10)+' cm</span><span class="pillx '+(good?'ok':'no')+'">'+d+' mm '+(good?'within':'over')+'</span></li>';
    }).join('');
    $('#msum').textContent=ok+' of '+T.rows.length+' measurements within '+tol+' mm.';
  };
  $('#tol').addEventListener('input',drawM); drawM();
}
if(T.type==='quiz'){
  var qi=0, score=0, answered=false, marks=[];
  root.innerHTML='<div class="qz" id="qz"></div>';
  var drawQ=function(){
    var z=$('#qz');
    var bar='<div class="qbar" aria-hidden="true">'+T.qs.map(function(q,i){return '<i class="'+(marks[i]||'')+'"></i>'}).join('')+'</div>';
    if(qi>=T.qs.length){
      z.innerHTML=bar+'<h3>You scored '+score+' of '+T.qs.length+'</h3><p class="muted">'+(score===T.qs.length?'Full marks. ':'')+'Try again or explore more content, as on the result page of the site.</p><div class="step-nav"><button class="btn" type="button" id="qa">Try again</button></div>';
      $('#qa').addEventListener('click',function(){qi=0;score=0;marks=[];drawQ()});return;
    }
    var q=T.qs[qi]; answered=false;
    z.innerHTML=bar+'<p class="mono">Question '+(qi+1)+' of '+T.qs.length+'</p><h3 class="qq">'+q[0]+'</h3><div class="opts">'+q[1].map(function(o,i){return '<button type="button" class="opt" data-i="'+i+'">'+o+'</button>'}).join('')+'</div><p class="note" id="qfb" aria-live="polite"></p><div class="step-nav"><button class="btn" type="button" id="qnx" hidden>'+(qi===T.qs.length-1?'See result':'Next question')+'</button></div>';
    Array.prototype.forEach.call(z.querySelectorAll('.opt'),function(b){b.addEventListener('click',function(){
      if(answered)return; answered=true; var i=+b.getAttribute('data-i'), ok=(i===q[2]);
      if(ok)score++; marks[qi]=ok?'ok':'bad';
      Array.prototype.forEach.call(z.querySelectorAll('.opt'),function(x,j){x.disabled=true; if(j===q[2])x.classList.add('ok'); else if(j===i)x.classList.add('bad')});
      z.querySelectorAll('.qbar i')[qi].className=marks[qi];
      $('#qfb').textContent=ok?'Right.':'Not this time. The right answer is '+q[1][q[2]]+'.';
      $('#qnx').hidden=false; $('#qnx').focus();
    })});
    $('#qnx').addEventListener('click',function(){qi++;drawQ()});
  };
  drawQ();
}
if(T.fig){ if(T.fig.stack) $('#try-fig').classList.add('stack'); $('#try-fig').innerHTML='<img src="'+T.fig.img+'" alt="'+T.fig.alt+'" loading="lazy"><div class="txt"><h3>'+T.fig.h+'</h3><p class="muted">'+T.fig.p+'</p></div>'; } else $('#try-fig').hidden=true;

/* ---------- build stepper ---------- */
var rail=$('#rail'), stepEl=$('#step'), si=0, L=D.steps;
L.forEach(function(l,i){
  var li=el('li'); var b=el('button',{type:'button','aria-label':'Step '+(i+1)+': '+l.t},String(i+1));
  b.addEventListener('click',function(){showStep(i)});
  li.appendChild(b); rail.appendChild(li);
});
function showStep(i){
  si=i; var l=L[i];
  Array.prototype.forEach.call(rail.querySelectorAll('button'),function(b,j){ if(j===i)b.setAttribute('aria-current','step'); else b.removeAttribute('aria-current')});
  var h='<div class="step-text"><span class="mono">Step '+(i+1)+' of '+L.length+'</span><h3>'+l.t+'</h3><p>'+l.p+'</p>';
  if(l.snag)h+='<div class="snag"><span class="mono">What went wrong</span><p>'+l.snag+'</p></div>';
  h+='<div class="step-nav"><button class="btn ghost" type="button" id="prev"'+(i===0?' disabled style="opacity:.4;cursor:default"':'')+'>Previous</button><button class="btn" type="button" id="next"'+(i===L.length-1?' disabled style="opacity:.4;cursor:default"':'')+'>Next</button></div>';
  if(l.below&&l.below.length){h+='<div class="step-below">'+l.below.map(function(m){return '<figure><img src="'+m[0]+'" alt="'+m[1]+'" loading="lazy"><figcaption>'+m[1]+'</figcaption></figure>'}).join('')+'</div>'}
  h+='</div>';
  h+='<div class="step-imgs'+(l.small?' sm':'')+'">';
  if(l.imgs&&l.imgs.length){l.imgs.forEach(function(m){h+='<figure><img src="'+m[0]+'" alt="'+m[1]+'" loading="lazy"><figcaption>'+m[1]+'</figcaption></figure>'})}
  else h+='<div class="noimg">'+(D.noimg||'No image for this step.')+'</div>';
  h+='</div>';
  stepEl.innerHTML=h;
  var p=$('#prev'),n=$('#next');
  if(p)p.addEventListener('click',function(){if(si>0)showStep(si-1)});
  if(n)n.addEventListener('click',function(){if(si<L.length-1)showStep(si+1)});
}
showStep(0);

/* ---------- changes ---------- */
var C=D.cmp, pvb=$('#pvb');
if(C){
$('#cmpSeg').innerHTML='<button class="chip" type="button" role="radio" aria-checked="false" data-s="plan">'+C.a+'</button><button class="chip" type="button" role="radio" aria-checked="true" data-s="built">'+C.b+'</button>';
$('#cmpHead').innerHTML='<tr><th>'+C.cols[0]+'</th><th class="plan">'+C.cols[1]+'</th><th class="built">'+C.cols[2]+'</th><th>'+C.cols[3]+'</th></tr>';
$('#cmp').innerHTML=C.rows.map(function(r){return '<tr><td>'+r[0]+'</td><td class="plan">'+r[1]+'</td><td class="built">'+r[2]+'</td><td>'+r[3]+'</td></tr>'}).join('');
$('#cmpImgs').innerHTML=(C.imgs||[]).map(function(m){return '<figure><img src="'+m[0]+'" alt="'+m[1]+'" loading="lazy"><figcaption>'+m[1]+'</figcaption></figure>'}).join('');
if(!(C.imgs||[]).length) $('#cmpImgs').hidden=true;
if(C.eq) $('#cmpImgs').className+=' eq';
function setState(s){pvb.setAttribute('data-state',s);Array.prototype.forEach.call(pvb.querySelectorAll('.chip'),function(b){b.setAttribute('aria-checked',b.getAttribute('data-s')===s?'true':'false')})}
Array.prototype.forEach.call(pvb.querySelectorAll('.chip'),function(b){b.addEventListener('click',function(){setState(b.getAttribute('data-s'))})});
setState('built');
}

/* ---------- tests ---------- */
var list=$('#tests-list'), okN=0;
D.tests.forEach(function(t,i){
  if(t.ok)okN++;
  var li=el('li'); li.setAttribute('data-ok',t.ok?'1':'0');
  var more='<div class="more"><p>'+t.d+'</p>'+(t.img?'<img src="'+t.img+'" alt="'+(t.alt||'')+'">':'')+'</div>';
  li.innerHTML='<details><summary><span class="id">T'+(i+1)+'</span><span class="c">'+t.c+'<small>'+t.m+'</small></span><span class="res">'+t.res+'</span><span class="pill'+(t.ok?'':' warn')+'">'+(t.pill||(t.ok?D.pills[0]:D.pills[1]))+'</span></summary>'+more+'</details>';
  list.appendChild(li);
});
$('#score').innerHTML=okN+' <small>of '+D.tests.length+' '+D.pills[0].toLowerCase()+'</small>';
var fBox=$('#filters');
[['all','All '+D.tests.length],['1',D.pills[0]+' '+okN],['0',D.pills[1]+' '+(D.tests.length-okN)]].forEach(function(f){
  var b=el('button',{'class':'chip',type:'button','aria-pressed':f[0]==='all'?'true':'false'},f[1]);
  b.addEventListener('click',function(){
    Array.prototype.forEach.call(fBox.children,function(x){x.setAttribute('aria-pressed',x===b?'true':'false')});
    Array.prototype.forEach.call(list.children,function(li){li.hidden=(f[0]!=='all'&&li.getAttribute('data-ok')!==f[0])});
  });
  fBox.appendChild(b);
});

/* ---------- reflection ---------- */
$('#improve').innerHTML=D.improve.map(function(x){return '<div class="item"><h3>'+x[0]+'</h3><p class="muted">'+x[1]+'</p></div>'}).join('');
$('#takeaways').innerHTML=D.take.map(function(x){return '<div class="item"><h3>'+x[0]+'</h3><p class="muted">'+x[1]+'</p></div>'}).join('');

/* ---------- copy email ---------- */
$('#copy').addEventListener('click',function(){
  var btn=this, node=$('#mail');
  function fallback(){var r=document.createRange(); r.selectNodeContents(node); var sl=window.getSelection(); sl.removeAllRanges(); sl.addRange(r); btn.textContent='Selected'}
  try{navigator.clipboard.writeText(node.textContent).then(function(){btn.textContent='Copied'},fallback)}catch(e){fallback()}
  setTimeout(function(){btn.textContent='Copy email'},2000);
});
})();
