// === Toggle mode clair / sombre ===
(function(){
  const btn = document.getElementById("lightModeToggle");
  const body = document.body;

  // Charger thème depuis localStorage
  if(localStorage.getItem("theme") === "light") {
    body.classList.add("light-mode");
    btn.textContent = "🌙";
  }

  btn.addEventListener("click", () => {
    body.classList.toggle("light-mode");
    if(body.classList.contains("light-mode")) {
      localStorage.setItem("theme", "light");
      btn.textContent = "🌙";
    } else {
      localStorage.setItem("theme", "dark");
      btn.textContent = "🌞";
    }
  });
})();
