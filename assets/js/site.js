(function(){
  var prog=document.getElementById('progress'), head=document.querySelector('header.site'), glow=document.getElementById('glow');
  var ticking=false;
  function onScroll(){
    var y=window.scrollY||0, h=document.documentElement.scrollHeight-window.innerHeight;
    if(prog) prog.style.transform='scaleX('+(h>0?y/h:0)+')';
    if(head) head.classList.toggle('scrolled', y>window.innerHeight*0.72);
    document.querySelectorAll('[data-para]').forEach(function(el){
      var r=el.parentElement.getBoundingClientRect();
      var off=(r.top+r.height/2-window.innerHeight/2)*parseFloat(el.getAttribute('data-para')||'0.08');
      el.style.transform='translateY('+off.toFixed(1)+'px)';
    });
    ticking=false;
  }
  window.addEventListener('scroll',function(){if(!ticking){ticking=true;requestAnimationFrame(onScroll);}},{passive:true});
  onScroll();
  if(glow&&window.matchMedia('(pointer:fine)').matches){
    window.addEventListener('mousemove',function(e){glow.style.left=e.clientX+'px';glow.style.top=e.clientY+'px';},{passive:true});
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
})();
