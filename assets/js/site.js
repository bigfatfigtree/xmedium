/* Extra Medium v12 — motion: reveals, parallax, count-ups, menu, clock, idea form.
   Reveal-hidden states exist ONLY under body.rv-on, added here before first paint settles. */
(function(){
  document.body.classList.add('rv-on');
  var reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ---- mobile menu ---- */
  var burger = document.querySelector('.burger'), menu = document.querySelector('.menu');
  function setMenu(open){
    if(!menu) return;
    menu.classList.toggle('open', open);
    menu.setAttribute('aria-hidden', open ? 'false' : 'true');
    if(burger) burger.setAttribute('aria-expanded', open ? 'true' : 'false');
    document.body.style.overflow = open ? 'hidden' : '';
  }
  if(burger) burger.addEventListener('click', function(){ setMenu(true); });
  if(menu){
    var close = menu.querySelector('.mclose');
    if(close) close.addEventListener('click', function(){ setMenu(false); });
    menu.querySelectorAll('a').forEach(function(a){ a.addEventListener('click', function(){ setMenu(false); }); });
  }
  document.addEventListener('keydown', function(e){ if(e.key === 'Escape') setMenu(false); });

  /* ---- Virginia Beach clock ---- */
  var clocks = document.querySelectorAll('.vbclock');
  if(clocks.length){
    var fmt = new Intl.DateTimeFormat('en-US', {timeZone:'America/New_York', hour:'2-digit', minute:'2-digit', second:'2-digit', hour12:true});
    var tick = function(){ var t = fmt.format(new Date()); clocks.forEach(function(c){ c.textContent = t; }); };
    tick(); setInterval(tick, 1000);
  }

  /* ---- scroll reveals ---- */
  var io = new IntersectionObserver(function(es){
    es.forEach(function(e){ if(e.isIntersecting){ e.target.classList.add('in'); io.unobserve(e.target); } });
  }, {threshold:.12});
  document.querySelectorAll('.rv,.rv-l,.rv-r').forEach(function(el){ io.observe(el); });

  /* ---- count-ups (final value is already the text content; animate from 0) ---- */
  var cio = new IntersectionObserver(function(es){
    es.forEach(function(e){
      if(!e.isIntersecting) return; cio.unobserve(e.target);
      var end = parseFloat(e.target.getAttribute('data-count')); if(isNaN(end)) return;
      if(reduced){ e.target.textContent = end; return; }
      var t0 = null;
      (function step(t){
        if(!t0) t0 = t;
        var p = Math.min((t - t0)/1200, 1);
        e.target.textContent = Math.round(end * (1 - Math.pow(1 - p, 3)));
        if(p < 1) requestAnimationFrame(step);
      })(performance.now());
    });
  }, {threshold:.4});
  document.querySelectorAll('[data-count]').forEach(function(el){ cio.observe(el); });

  /* ---- motion engine: image parallax, layered collages, floating shapes ---- */
  if(!reduced){
    var vh = window.innerHeight;
    window.addEventListener('resize', function(){ vh = window.innerHeight; });
    var px = Array.prototype.slice.call(document.querySelectorAll('[data-plx]'));
    /* layered collages */
    var fine = window.matchMedia('(pointer:fine)').matches;
    var sets = [];
    document.querySelectorAll('[data-layers]').forEach(function(el, idx){
      var st = {el: el, bg: el.querySelector('.lbg'), fg: el.querySelector('.lfg'), tx: 0, ty: 0, cx: 0, cy: 0, seed: idx * 1.7};
      if(fine){
        el.addEventListener('pointermove', function(e){
          var r = el.getBoundingClientRect();
          st.tx = ((e.clientX - r.left) / r.width - .5) * 16;
          st.ty = ((e.clientY - r.top) / r.height - .5) * 12;
        });
        el.addEventListener('pointerleave', function(){ st.tx = 0; st.ty = 0; });
      }
      sets.push(st);
    });
    /* floating shapes injected into plain collage frames */
    var shapes = [];
    var defs = [
      {cls: 'fx fx-disc', w: 96, h: 96, pos: {top: '-30px', right: '-22px'}, rate: -26, spin: 16, rot: 0},
      {cls: 'fx fx-ring', w: 58, h: 58, pos: {bottom: '-16px', left: '-14px'}, rate: 20, spin: -22, rot: 0},
      {cls: 'fx fx-bar', w: 86, h: 26, pos: {bottom: '11%', right: '-18px'}, rate: -13, spin: 5, rot: -4}
    ];
    document.querySelectorAll('.fxf').forEach(function(fr){
      defs.forEach(function(d){
        var sp = document.createElement('span');
        sp.className = d.cls;
        sp.style.width = d.w + 'px'; sp.style.height = d.h + 'px';
        Object.keys(d.pos).forEach(function(k){ sp.style[k] = d.pos[k]; });
        sp.appendChild(document.createElement('i'));
        fr.appendChild(sp);
        shapes.push({el: sp, host: fr, rate: d.rate, spin: d.spin, rot: d.rot});
      });
    });
    var loop = function(t){
      px.forEach(function(img){
        var host = img.closest('.frame,.band-media') || img.parentElement;
        var r = host.getBoundingClientRect();
        if(r.bottom < -120 || r.top > vh + 120) return;
        var off = (r.top + r.height / 2 - vh / 2) * parseFloat(img.getAttribute('data-plx'));
        var sc = img.classList.contains('bandimg') ? 1.15 : 1.14;
        var rot = img.closest('.fxf') ? ' rotate(' + (((r.top + r.height / 2 - vh / 2) / vh) * 1.1).toFixed(2) + 'deg)' : '';
        img.style.transform = 'scale(' + sc + ') translateY(' + off.toFixed(1) + 'px)' + rot;
      });
      sets.forEach(function(st){
        var r = st.el.getBoundingClientRect();
        if(r.bottom < -80 || r.top > vh + 80) return;
        var p = (r.top + r.height / 2 - vh / 2) / vh;
        st.cx += (st.tx - st.cx) * .055;
        st.cy += (st.ty - st.cy) * .055;
        var bob = Math.sin(t / 1500 + st.seed) * 4;
        if(st.bg) st.bg.style.transform = 'translate3d(0,' + (p * -10).toFixed(1) + 'px,0) scale(1.07)';
        if(st.fg) st.fg.style.transform = 'translate3d(' + (st.cx + p * 7).toFixed(1) + 'px,' + (st.cy + bob + p * 17).toFixed(1) + 'px,0) rotate(' + (p * 1.25).toFixed(2) + 'deg) scale(1.05)';
      });
      shapes.forEach(function(sh){
        var r = sh.host.getBoundingClientRect();
        if(r.bottom < -80 || r.top > vh + 80) return;
        var p = (r.top + r.height / 2 - vh / 2) / vh;
        sh.el.style.transform = 'translate3d(0,' + (p * sh.rate).toFixed(1) + 'px,0) rotate(' + (sh.rot + p * sh.spin).toFixed(1) + 'deg)';
      });
      requestAnimationFrame(loop);
    };
    requestAnimationFrame(loop);
  }

  /* ---- footer idea form: AJAX submit, Netlify Forms ---- */
  var ideaForm = document.querySelector('form.idea-form');
  if(ideaForm){
    if(/[?&]idea=1/.test(location.search)) showIdeaDone();
    ideaForm.addEventListener('submit', function(ev){
      ev.preventDefault();
      var data = new FormData(ideaForm);
      fetch('/', {method:'POST', headers:{'Content-Type':'application/x-www-form-urlencoded'},
        body: new URLSearchParams(data).toString()})
        .then(function(r){ if(r.ok) showIdeaDone(); else ideaForm.submit(); })
        .catch(function(){ ideaForm.submit(); });
    });
    function showIdeaDone(){
      var cap = document.getElementById('ideaCap'); if(!cap) return;
      var done = document.createElement('p');
      done.className = 'idea-done';
      done.textContent = "You're in. First idea lands this week — steal it well.";
      ideaForm.replaceWith(done);
    }
  }
})();
