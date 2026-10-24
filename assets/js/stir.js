/* STIR — Extra Medium's living pigment field. Canvas 2D flow field, no libraries.
   Particles drift through a slow noise field; pointer/touch stirs; palette shifts per section. */
(function(){
  var canvas=document.getElementById('field');
  if(!canvas) return;
  var reduced=window.matchMedia&&window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var ctx=canvas.getContext('2d');
  if(!ctx||reduced){ document.body.classList.add('noanim'); return; }
  var W=0,H=0,DPR=1,parts=[],mouse={x:-9999,y:-9999,vx:0,vy:0,px:0,py:0},t=0;
  var PAL_EM=[[255,122,24],[255,61,138],[176,80,255]];
  var PAL_SG=[[37,99,235],[13,180,160],[34,197,94]];
  var palMix=0,palTarget=0;
  var calmEl=document.querySelector('.calm'),calmRect=null;
  function ramp(pal,s,a){
    var seg=Math.min(1.999,Math.max(0,s*2)),i=Math.floor(seg),f=seg-i;
    var c1=pal[i],c2=pal[Math.min(2,i+1)];
    return 'rgba('+Math.round(c1[0]+(c2[0]-c1[0])*f)+','+Math.round(c1[1]+(c2[1]-c1[1])*f)+','+Math.round(c1[2]+(c2[2]-c1[2])*f)+','+a+')';
  }
  function mixPal(s,a){
    var pal=[0,1,2].map(function(i){ return [0,1,2].map(function(j){ return Math.round(PAL_EM[i][j]+(PAL_SG[i][j]-PAL_EM[i][j])*palMix); }); });
    return ramp(pal,s,a);
  }
  function sizeCanvas(){
    DPR=Math.min(1.75,window.devicePixelRatio||1);
    W=window.innerWidth; H=window.innerHeight;
    canvas.width=W*DPR; canvas.height=H*DPR;
    canvas.style.width=W+'px'; canvas.style.height=H+'px';
    ctx.setTransform(DPR,0,0,DPR,0,0);
    var target=Math.round(Math.min(1500,Math.max(420,(W*H)/1850)));
    while(parts.length<target) parts.push(newPart(true));
    parts.length=target;
    measureCalm();
  }
  function measureCalm(){ if(calmEl){ var r=calmEl.getBoundingClientRect(); calmRect={x:r.left-30,y:r.top-20,w:r.width+60,h:r.height+40}; } }
  function newPart(anywhere){
    return {x:Math.random()*W,y:anywhere?Math.random()*H:-10,vx:0,vy:0,life:0,max:260+Math.random()*300};
  }
  function angle(x,y){
    return (Math.cos(x*0.0016+t*0.10)+Math.sin(y*0.0021-t*0.08))*Math.PI;
  }
  var lastBurst=0;
  function burst(x,y,n,power){
    for(var i=0;i<parts.length;i++){ var p=parts[i],dx=p.x-x,dy=p.y-y,d2=dx*dx+dy*dy;
      if(d2<12100){ var d=Math.sqrt(d2)||1,f=(1-d/110)*power; p.vx+=(dx/d)*f; p.vy+=(dy/d)*f; } }
    lastBurst=performance.now();
  }
  window.__stirBurst=function(x,y){ burst(x,y,0,7); };
  window.addEventListener('pointermove',function(e){
    mouse.vx=e.clientX-mouse.px; mouse.vy=e.clientY-mouse.py; mouse.px=mouse.x=e.clientX; mouse.py=mouse.y=e.clientY;
  },{passive:true});
  window.addEventListener('pointerdown',function(e){ burst(e.clientX,e.clientY,0,9); },{passive:true});
  var lastY=window.scrollY||0,lastStir=0,stirSide=1;
  window.addEventListener('scroll',function(){ measureCalm(); var y=window.scrollY||0,dy=Math.abs(y-lastY); lastY=y; var now=performance.now();
    if(dy>14&&now-lastStir>110){ lastStir=now; stirSide*=-1; burst(W*(stirSide>0?0.84:0.16),H*0.45,0,Math.min(11,2.5+dy*0.10)); } },{passive:true});
  /* palette follows sections */
  if('IntersectionObserver' in window){
    var po=new IntersectionObserver(function(es){ es.forEach(function(en){ if(en.isIntersecting){ palTarget=en.target.getAttribute('data-pal')==='signl'?1:0; } }); },{threshold:.35});
    document.querySelectorAll('[data-pal]').forEach(function(el){ po.observe(el); });
    /* stamp-in lines */
    var so=new IntersectionObserver(function(es){ es.forEach(function(en){ if(en.isIntersecting){ var el=en.target; setTimeout(function(){ el.classList.add('in'); },(parseInt(el.getAttribute('data-d')||'0',10))*160); so.unobserve(el); } }); },{threshold:.4});
    document.querySelectorAll('[data-stamp]').forEach(function(el){ so.observe(el); });
  }
  var frames=0,slowFrames=0,last=performance.now(),running=true;
  document.addEventListener('visibilitychange',function(){ running=!document.hidden; if(running){ last=performance.now(); requestAnimationFrame(step); } });
  function step(now){
    if(!running) return;
    var dt=now-last; last=now; frames++;
    if(dt>26){ slowFrames++; } else { slowFrames=Math.max(0,slowFrames-1); }
    if(slowFrames>90&&parts.length>380){ parts.length=Math.floor(parts.length*0.8); slowFrames=0; }
    t+=0.008;
    palMix+=(palTarget-palMix)*0.02;
    ctx.fillStyle='rgba(255,248,240,0.10)';
    ctx.fillRect(0,0,W,H);
    /* idle life: a slow figure-eight emitter stirs the vat */
    var ex=W*0.5+Math.cos(t*0.7)*W*0.30, ey=H*0.42+Math.sin(t*1.4)*H*0.20;
    if(frames%3===0) burst(ex,ey,0,0.55);
    ctx.lineWidth=2.3; ctx.lineCap='round';
    for(var i=0;i<parts.length;i++){
      var p=parts[i],a=angle(p.x,p.y);
      p.vx+=Math.cos(a)*0.055; p.vy+=Math.sin(a)*0.055;
      var dxm=p.x-mouse.x,dym=p.y-mouse.y,dm2=dxm*dxm+dym*dym;
      if(dm2<19600){ p.vx+=mouse.vx*0.014*(1-Math.sqrt(dm2)/140); p.vy+=mouse.vy*0.014*(1-Math.sqrt(dm2)/140); }
      if(calmRect&&p.x>calmRect.x&&p.x<calmRect.x+calmRect.w&&p.y>calmRect.y&&p.y<calmRect.y+calmRect.h){ p.vx*=0.90; p.vy*=0.90; }
      p.vx*=0.94; p.vy*=0.94;
      var sp=Math.sqrt(p.vx*p.vx+p.vy*p.vy);
      var nx=p.x+p.vx,ny=p.y+p.vy;
      if(sp>0.16){
        ctx.strokeStyle=mixPal(Math.min(1,sp/7),Math.min(0.88,0.22+sp*0.11));
        ctx.beginPath(); ctx.moveTo(p.x,p.y); ctx.lineTo(nx,ny); ctx.stroke();
      }
      p.x=nx; p.y=ny; p.life++;
      if(p.x<-20||p.x>W+20||p.y<-20||p.y>H+20||p.life>p.max){ parts[i]=newPart(false); if(Math.random()<0.5){ parts[i].y=H+10; parts[i].x=Math.random()*W; } }
    }
    mouse.vx*=0.8; mouse.vy*=0.8;
    requestAnimationFrame(step);
  }
  sizeCanvas();
  window.addEventListener('resize',sizeCanvas);
  ctx.fillStyle='#fff8f0'; ctx.fillRect(0,0,W,H);
  requestAnimationFrame(step);
})();
