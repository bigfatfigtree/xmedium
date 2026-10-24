(function(){
  var prog=document.getElementById('progress'), glow=document.getElementById('glow');
  var scrolly=document.querySelector('.scrolly'), chaps=document.querySelectorAll('.chap'), cdots=document.querySelectorAll('.chap-dots i'), ccount=document.querySelector('.chap-count');
  var bigw=document.querySelector('.bigword'), bigfill=document.querySelector('.bigword .fillw');
  var fine=window.matchMedia('(pointer:fine)').matches;
  var ticking=false;
  function clamp01(x){return Math.max(0,Math.min(1,x));}
  function onScroll(){
    var y=window.scrollY||0, h=document.documentElement.scrollHeight-window.innerHeight;
    if(prog) prog.style.transform='scaleX('+(h>0?y/h:0)+')';
    document.querySelectorAll('img[data-para]').forEach(function(el){
      var r=el.parentElement.getBoundingClientRect();
      var off=(r.top+r.height/2-window.innerHeight/2)*parseFloat(el.getAttribute('data-para')||'0.08');
      el.style.transform='translateY('+off.toFixed(1)+'px)';
    });
    if(scrolly&&chaps.length){
      var r=scrolly.getBoundingClientRect();
      var p=clamp01(-r.top/(scrolly.offsetHeight-window.innerHeight));
      var idx=Math.min(chaps.length-1,Math.floor(p*chaps.length));
      chaps.forEach(function(c,i){c.classList.toggle('on',i===idx);});
      cdots.forEach(function(d,i){d.classList.toggle('on',i===idx);});
      if(ccount) ccount.textContent='0'+(idx+1)+' / 0'+chaps.length;
    }
    if(bigw&&bigfill){
      var r2=bigw.getBoundingClientRect();
      var p2=clamp01((window.innerHeight*0.92-r2.top)/(window.innerHeight*0.75));
      bigfill.style.clipPath='inset(0 '+((1-p2)*100).toFixed(1)+'% 0 0)';
    }
    ticking=false;
  }
  window.addEventListener('scroll',function(){if(!ticking){ticking=true;requestAnimationFrame(onScroll);}},{passive:true});
  onScroll();
  /* menu */
  var burger=document.querySelector('.burger');
  if(burger){ burger.addEventListener('click',function(){ var open=document.body.classList.toggle('menu-open'); burger.setAttribute('aria-expanded',open?'true':'false'); burger.innerHTML=open?'&#10005;':'&#9776;'; }); }
  document.querySelectorAll('.menu a').forEach(function(a){ a.addEventListener('click',function(){ document.body.classList.remove('menu-open'); }); });
/* THE SENTENCE: the hero corrects itself */
var tw=document.getElementById('tw');
if(tw&&!reduced){
  var finalWord='un-ignorable.', draftWord='noticeable.';
  tw.textContent=draftWord; tw.classList.remove('gtext'); tw.style.fontStyle='normal'; tw.classList.add('typing');
  function delWord(txt,done){ var i=txt.length; (function d(){ i--; tw.textContent=txt.slice(0,i)||'\u00a0'; if(i>0){ setTimeout(d,34); } else { done(); } })(); }
  function typeWord(txt,done){ var i=0; (function tp(){ i++; tw.textContent=txt.slice(0,i); if(i<txt.length){ setTimeout(tp,52); } else { done(); } })(); }
  setTimeout(function(){ delWord(draftWord,function(){ tw.classList.add('gtext'); tw.style.fontStyle='italic'; typeWord(finalWord,function(){ tw.classList.remove('typing'); tw.classList.add('boom'); }); }); },1150);
}
/* IDEA SNACK dispenser */
var snackBtn=document.getElementById('snackBtn'), snackCard=document.getElementById('snackCard');
if(snackBtn&&snackCard){
  var ideas=[
    'Rename your loyalty program after your best customer. Watch what happens.',
    'Put your worst review on a t-shirt. Sell it. People love a brand that can take a punch.',
    'Your About page is where brands go to be boring. Rewrite it as a letter to one person.',
    'Name a menu item after the regular who orders it most. Never take it off.',
    'Stop posting your product. Post the moment right before your customer needs it.',
    'Send your happiest customer a handwritten note with nothing to buy. Screenshot the reply. That is your ad.',
    'Let customers name your next special and vote in public. Their friends become your reach.',
    'Make your out-of-office reply so good people forward it. Most brands waste their funniest surface.',
    'Print your first-ever terrible idea on the wall. Confidence is a brand asset.',
    'Give one customer a skip-the-line-forever pass for a dollar. Film everyone reacting.'
  ];
  var lastIdea=-1;
  snackBtn.addEventListener('click',function(){
    var i; do{ i=Math.floor(Math.random()*ideas.length); }while(i===lastIdea); lastIdea=i;
    document.getElementById('snackIdea').textContent=ideas[i];
    var d=new Date().toLocaleDateString('en-US',{month:'long',day:'numeric',year:'numeric'});
    document.getElementById('snackStamp').textContent='Dispensed by Extra Medium - '+d+' - No refunds on genius.';
    snackCard.classList.remove('show'); void snackCard.offsetWidth; snackCard.classList.add('show');
    if(window.__stirBurst){ var r=snackBtn.getBoundingClientRect(); window.__stirBurst(r.left+r.width/2,r.top+r.height/2); }
    snackBtn.textContent='Dispense another';
  });
}
  /* Virginia Beach clock */
  var clock=document.getElementById('vbclock');
  function tickClock(){ try{ var t=new Date().toLocaleTimeString('en-US',{timeZone:'America/New_York',hour:'2-digit',minute:'2-digit',second:'2-digit',hour12:false}); document.querySelectorAll('.vbclock').forEach(function(el){el.textContent=t;}); }catch(e){} }
  tickClock(); setInterval(tickClock,1000);
  /* autoplay hardening: force muted via JS, retry on first touch, hide videos the browser refuses to play (animated stills take over — no dead play-button overlays) */
  var heroV=document.querySelector('.hero-full video');
  function markFail(v){ var n=parseInt(v.getAttribute('data-fail')||'0',10)+1; v.setAttribute('data-fail',String(n)); if(n>=2){ v.style.display='none'; } if(v===heroV){ document.body.classList.add('novideo'); } }
  function tryPlay(v){ if(!v||v.style.display==='none')return; v.muted=true; try{v.setAttribute('muted','');}catch(e){} v.playsInline=true; var p; try{p=v.play();}catch(e){ markFail(v); return; } if(p&&p.catch)p.catch(function(){ markFail(v); }); }
  if(heroV){ tryPlay(heroV); setTimeout(function(){ if(heroV.paused&&heroV.readyState>=2){ document.body.classList.add('novideo'); heroV.style.display='none'; } },1600); }
  ['pointerdown','touchstart'].forEach(function(ev){ window.addEventListener(ev,function(){ document.querySelectorAll('video').forEach(function(v){ if(v.style.display==='none'&&parseInt(v.getAttribute('data-fail')||'0',10)<3){ v.style.display=''; } tryPlay(v); }); if(heroV&&!heroV.paused){ document.body.classList.remove('novideo'); } },{passive:true}); });
  /* videos: play when visible, pause when not (mobile-safe, muted autoplay) */
  var vio=new IntersectionObserver(function(es){
    es.forEach(function(en){
      var v=en.target;
      if(en.isIntersecting){ tryPlay(v); }
      else if(!v.paused){ v.pause(); }
    });
  },{threshold:.12});
  document.querySelectorAll('video').forEach(function(v){ vio.observe(v); });
  /* rotating headline word */
  var rot=document.getElementById('rotword');
  if(rot){
    var words=['noticing.','talking about.','remembering.','sharing.','paying for.'], wi=0;
    setInterval(function(){
      rot.classList.add('flip');
      setTimeout(function(){ wi=(wi+1)%words.length; rot.textContent=words[wi]; rot.classList.remove('flip'); },360);
    },3400);
  }
  /* reveals + counters */
  var io=new IntersectionObserver(function(es){
    es.forEach(function(en){
      if(!en.isIntersecting) return;
      en.target.classList.add('in'); io.unobserve(en.target);
      en.target.querySelectorAll('[data-count]').forEach(runCounter);
      if(en.target.hasAttribute('data-count')) runCounter(en.target);
    });
  },{threshold:.18});
  document.querySelectorAll('.rv, [data-count]').forEach(function(el){io.observe(el);});
  function runCounter(el){
    if(el.dataset.done) return; el.dataset.done=1;
    var target=parseFloat(el.getAttribute('data-count')), suf=el.getAttribute('data-suffix')||'', t0=null, dur=1400;
    function step(ts){ if(!t0)t0=ts; var p=Math.min((ts-t0)/dur,1), e=1-Math.pow(1-p,3);
      el.textContent=Math.round(target*e)+suf; if(p<1) requestAnimationFrame(step); }
    requestAnimationFrame(step);
  }
  /* tilt */
  document.querySelectorAll('.tilt').forEach(function(card){
    card.addEventListener('mousemove',function(e){
      var r=card.getBoundingClientRect(), x=(e.clientX-r.left)/r.width-.5, y=(e.clientY-r.top)/r.height-.5;
      card.style.transform='perspective(1200px) rotateY('+(x*4)+'deg) rotateX('+(-y*4)+'deg)';
    });
    card.addEventListener('mouseleave',function(){card.style.transform='';});
  });
  if(fine){

    /* glow + cursor ring + magnetic buttons */
    var ring=document.getElementById('cursor'), mx=innerWidth/2,my=innerHeight/2,rx=mx,ry=my;
    window.addEventListener('mousemove',function(e){
      mx=e.clientX; my=e.clientY;
      if(glow){glow.style.left=mx+'px';glow.style.top=my+'px';}
      if(ring){ ring.classList.toggle('big', !!e.target.closest('a,button,summary')); }
    },{passive:true});
    (function loop(){ rx+=(mx-rx)*.16; ry+=(my-ry)*.16; if(ring){ring.style.left=rx+'px';ring.style.top=ry+'px';} requestAnimationFrame(loop); })();
    document.querySelectorAll('.btn').forEach(function(b){
      b.addEventListener('mousemove',function(e){ var r=b.getBoundingClientRect(); b.style.transform='translate('+((e.clientX-r.left)/r.width-.5)*7+'px,'+((e.clientY-r.top)/r.height-.5)*7+'px)'; });
      b.addEventListener('mouseleave',function(){ b.style.transform=''; });
    });
  }
  if(window.matchMedia('(prefers-reduced-motion: reduce)').matches){
    document.querySelectorAll('.rv').forEach(function(el){el.classList.add('in');});
  }
})();
