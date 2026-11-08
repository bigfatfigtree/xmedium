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

  /* ---- parallax on [data-plx] images ---- */
  if(!reduced){
    var px = Array.prototype.slice.call(document.querySelectorAll('[data-plx]'));
    if(px.length){
      var ticking = false;
      var upd = function(){
        ticking = false; var vh = window.innerHeight;
        px.forEach(function(img){
          var host = img.closest('.frame,.band-media') || img.parentElement;
          var r = host.getBoundingClientRect();
          if(r.bottom < -120 || r.top > vh + 120) return;
          var off = (r.top + r.height/2 - vh/2) * parseFloat(img.getAttribute('data-plx'));
          var sc = img.classList.contains('bandimg') ? 1.15 : 1.14;
          img.style.transform = 'scale(' + sc + ') translateY(' + off.toFixed(1) + 'px)';
        });
      };
      window.addEventListener('scroll', function(){ if(!ticking){ ticking = true; requestAnimationFrame(upd); } }, {passive:true});
      window.addEventListener('resize', upd);
      upd();
    }
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
