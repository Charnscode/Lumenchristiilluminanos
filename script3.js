document.getElementById('year').textContent = new Date().getFullYear();

 toggle nav mobile var toggle = document.querySelector('.nav-toggle'); var nav = document.querySelector('.nav'); toggle && toggle.addEventListener('click', function(){ nav.classList.toggle('open'); });

form submission (simulé, léger) window.submitForm = function(e){ e.preventDefault(); var status = document.getElementById('formStatus'); status.textContent = 'Envoi en cours...';  simulation légère sans appel réseau setTimeout(function(){ status.textContent = 'Merci ! Ton message a été reçu (simulation).'; e.target.reset(); },700); return false; };

 for internal links document.querySelectorAll('a[href^="#"]').forEach(function(a){ a.addEventListener('click', function(e){ var tgt = document.querySelector(this.getAttribute('href')); if(tgt){ e.preventDefault(); tgt.scrollIntoView({behavior:'smooth',block:'start'});  nav.classList.remove('open'); } }); }); })();

