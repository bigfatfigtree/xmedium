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

  /* ---- motion engine: pieces split apart as a collage leaves center, reassemble as it arrives ---- */
  if(!reduced){
    var vh = window.innerHeight;
    window.addEventListener('resize', function(){ vh = window.innerHeight; });
    var px = Array.prototype.slice.call(document.querySelectorAll('[data-plx]'));
    var fine = window.matchMedia('(pointer:fine)').matches;
    var sets = [];
    document.querySelectorAll('[data-layers]').forEach(function(el, idx){
      var st = {el: el, bg: el.querySelector('.lbg'), rest: el.querySelector('.lrest'),
                tx: 0, ty: 0, cx: 0, cy: 0, pieces: []};
      el.querySelectorAll('.lp').forEach(function(im, i){
        st.pieces.push({el: im, dx: parseFloat(im.getAttribute('data-dx')), dy: parseFloat(im.getAttribute('data-dy')),
                        rot: parseFloat(im.getAttribute('data-rot')), ph: idx * 1.31 + i * 0.97});
      });
      if(fine){
        el.addEventListener('pointermove', function(e){
          var r = el.getBoundingClientRect();
          st.tx = ((e.clientX - r.left) / r.width - .5) * 18;
          st.ty = ((e.clientY - r.top) / r.height - .5) * 13;
        });
        el.addEventListener('pointerleave', function(){ st.tx = 0; st.ty = 0; });
      }
      sets.push(st);
    });
    var loop = function(t){
      px.forEach(function(img){
        var host = img.closest('.frame,.band-media') || img.parentElement;
        var r = host.getBoundingClientRect();
        if(r.bottom < -120 || r.top > vh + 120) return;
        var off = (r.top + r.height / 2 - vh / 2) * parseFloat(img.getAttribute('data-plx'));
        var sc = img.classList.contains('bandimg') ? 1.15 : 1.14;
        img.style.transform = 'scale(' + sc + ') translateY(' + off.toFixed(1) + 'px)';
      });
      sets.forEach(function(st){
        var r = st.el.getBoundingClientRect();
        if(r.bottom < -60 || r.top > vh + 60) return;
        var q = (r.top + r.height / 2 - vh / 2) / (vh * 0.58);
        q = Math.max(-1, Math.min(1, q));
        var aq = Math.abs(q), e = aq * aq * (3 - 2 * aq);
        st.cx += (st.tx - st.cx) * .05;
        st.cy += (st.ty - st.cy) * .05;
        if(st.bg) st.bg.style.transform = 'translate3d(0,' + (q * 9).toFixed(1) + 'px,0) scale(1.06)';
        if(st.rest) st.rest.style.transform = 'translate3d(0,' + (q * -11).toFixed(1) + 'px,0)';
        st.pieces.forEach(function(pc){
          var ix = Math.sin(t / 1700 + pc.ph) * 2.2, iy = Math.cos(t / 1900 + pc.ph) * 2.2;
          var ir = Math.sin(t / 2300 + pc.ph) * .35;
          pc.el.style.transform = 'translate3d(' + (pc.dx * e + st.cx + ix).toFixed(1) + 'px,' + (pc.dy * e + st.cy + iy).toFixed(1) + 'px,0) rotate(' + (pc.rot * e + ir).toFixed(2) + 'deg)';
        });
      });
      requestAnimationFrame(loop);
    };
    requestAnimationFrame(loop);
  }

  /* ---- branded form confirmations: AJAX submit, Netlify Forms ---- */
  function donePanel(mini, headHTML, bodyText, linkHref, linkText){
    var d = document.createElement('div');
    d.className = 'form-done' + (mini ? ' mini' : '');
    d.setAttribute('role', 'status');
    var img = document.createElement('img');
    img.src = '/assets/img/em-icon-shout.png'; img.alt = '';
    d.appendChild(img);
    if(!mini){
      var k = document.createElement('p'); k.className = 'fd-kick';
      k.textContent = 'Extra! Extra!'; d.appendChild(k);
    }
    var h = document.createElement('p'); h.className = 'fd-head';
    h.innerHTML = headHTML; d.appendChild(h);
    var b = document.createElement('p'); b.className = 'fd-body';
    b.textContent = bodyText; d.appendChild(b);
    if(linkHref){
      var a = document.createElement('a'); a.className = 'fd-link';
      a.href = linkHref; a.textContent = linkText; d.appendChild(a);
    }
    return d;
  }
  function wireForm(form, makePanel, sentParam){
    if(!form) return;
    if(sentParam && new RegExp('[?&]' + sentParam).test(location.search)){
      var p = makePanel(); form.replaceWith(p);
      p.scrollIntoView({block: 'center'});
      return;
    }
    form.addEventListener('submit', function(ev){
      ev.preventDefault();
      var data = new FormData(form);
      fetch('/', {method: 'POST', headers: {'Content-Type': 'application/x-www-form-urlencoded'},
        body: new URLSearchParams(data).toString()})
        .then(function(r){
          if(r.ok){ var p = makePanel(); form.replaceWith(p); p.scrollIntoView({block: 'center'}); }
          else form.submit();
        })
        .catch(function(){ form.submit(); });
    });
  }
  var leadForm = document.querySelector('form.lead');
  wireForm(leadForm, function(){
    return donePanel(false, 'Consider it <em>shouted.</em>',
      'Your note just landed. A human reads every one \u2014 usually the founder \u2014 and replies within one business day.',
      '/magazine/', 'While you wait, read Extra Extra \u2192');
  }, 'sent=1');
  var ideaForm = document.querySelector('form.idea-form');
  wireForm(ideaForm, function(){
    return donePanel(true, 'You\u2019re in.',
      'First idea lands this week \u2014 steal it well.', null, null);
  }, 'idea=1');
})();
