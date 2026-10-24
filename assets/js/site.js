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
  if(burger){ burger.addEventListener('click',function(){ document.body.classList.toggle('menu-open'); }); }
  document.querySelectorAll('.menu a').forEach(function(a){ a.addEventListener('click',function(){ document.body.classList.remove('menu-open'); }); });
  /* Virginia Beach clock */
  var clock=document.getElementById('vbclock');
  function tickClock(){ try{ var t=new Date().toLocaleTimeString('en-US',{timeZone:'America/New_York',hour:'2-digit',minute:'2-digit',second:'2-digit',hour12:false}); document.querySelectorAll('.vbclock').forEach(function(el){el.textContent=t;}); }catch(e){} }
  tickClock(); setInterval(tickClock,1000);
  /* videos: play when visible, pause when not (mobile-safe, muted autoplay) */
  var vio=new IntersectionObserver(function(es){
    es.forEach(function(en){
      var v=en.target;
      if(en.isIntersecting){ if(v.paused) v.play().catch(function(){}); }
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
