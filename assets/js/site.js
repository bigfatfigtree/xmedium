(function(){
  var prog=document.getElementById('progress'), head=document.querySelector('header.site'), glow=document.getElementById('glow');
  var scrolly=document.querySelector('.scrolly'), chaps=document.querySelectorAll('.chap'), cdots=document.querySelectorAll('.chap-dots i'), ccount=document.querySelector('.chap-count');
  var bigw=document.querySelector('.bigword'), bigfill=document.querySelector('.bigword .fillw');
  var ticking=false;
  function clamp01(x){return Math.max(0,Math.min(1,x));}
  function onScroll(){
    var y=window.scrollY||0, h=document.documentElement.scrollHeight-window.innerHeight;
    if(prog) prog.style.transform='scaleX('+(h>0?y/h:0)+')';
    if(head) head.classList.toggle('scrolled', y>window.innerHeight*0.72);
    document.querySelectorAll('[data-para]').forEach(function(el){
      var r=el.parentElement.getBoundingClientRect();
      var off=(r.top+r.height/2-window.innerHeight/2)*parseFloat(el.getAttribute('data-para')||'0.08');
      el.style.transform='translateY('+off.toFixed(1)+'px) scale(1.12)';
    });
    if(scrolly&&chaps.length){
      var r=scrolly.getBoundingClientRect();
      var p=clamp01(-r.top/(scrolly.offsetHeight-window.innerHeight));
      var idx=Math.min(chaps.length-1,Math.floor(p*chaps.length));
      chaps.forEach(function(c,i){c.classList.toggle('on',i===idx); var v=c.querySelector('video'); if(v){ if(i===idx&&v.paused)v.play().catch(function(){}); else if(i!==idx&&!v.paused)v.pause(); }});
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
  if(glow&&window.matchMedia('(pointer:fine)').matches){
    window.addEventListener('mousemove',function(e){glow.style.left=e.clientX+'px';glow.style.top=e.clientY+'px';},{passive:true});
  }
  /* hero montage */
  var hvids=document.querySelectorAll('.hero-vid'), hdots=document.querySelectorAll('.hero-dots i'), hi=0;
  if(hvids.length>1){
    setInterval(function(){
      hvids[hi].classList.remove('on'); if(hdots[hi])hdots[hi].classList.remove('on');
      hi=(hi+1)%hvids.length;
      var v=hvids[hi]; v.classList.add('on'); if(hdots[hi])hdots[hi].classList.add('on');
      if(v.paused) v.play().catch(function(){});
    },6000);
  }
  /* rotating headline word */
  var rot=document.getElementById('rotword');
  if(rot){
    var words=['noticing.','talking about.','remembering.','sharing.','paying for.'], wi=0;
    setInterval(function(){
      rot.classList.add('flip');
      setTimeout(function(){ wi=(wi+1)%words.length; rot.textContent=words[wi]; rot.classList.remove('flip'); },360);
    },3400);
  }
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
  document.querySelectorAll('.tilt').forEach(function(card){
    card.addEventListener('mousemove',function(e){
      var r=card.getBoundingClientRect(), x=(e.clientX-r.left)/r.width-.5, y=(e.clientY-r.top)/r.height-.5;
      card.style.transform='perspective(1200px) rotateY('+(x*4)+'deg) rotateX('+(-y*4)+'deg)';
    });
    card.addEventListener('mouseleave',function(){card.style.transform='';});
  });
  if(window.matchMedia('(prefers-reduced-motion: reduce)').matches){
    document.querySelectorAll('.rv').forEach(function(el){el.classList.add('in');});
    document.querySelectorAll('.chap').forEach(function(c,i){if(i===0)c.classList.add('on');});
  }
})();
