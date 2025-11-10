
// --- Bouton retour en haut ---
const backToTop = document.createElement("button");
backToTop.id = "backToTop";
backToTop.textContent = "Haut";
document.body.appendChild(backToTop);

window.addEventListener("scroll", () => {
  if (window.scrollY > 300) {
    backToTop.style.display = "block";
  } else {
    backToTop.style.display = "none";
  }
});

backToTop.addEventListener("click", () => {
  window.scrollTo({ top: 0, behavior: "smooth" });
});

document.body.style.transition = "background 1.5s ease-in-out";

// --- Animation d’apparition des éléments ---
const elements = document.querySelectorAll("h2, h3, p, video");

function checkScroll() {
  const triggerBottom = window.innerHeight * 0.85;
  elements.forEach((el) => {
    const rect = el.getBoundingClientRect();
    if (rect.top < triggerBottom) {
      el.classList.add("visible");
    }
  });
}

window.addEventListener("scroll", checkScroll);
checkScroll();

// --- Liste des miracles ---
const miracles = [
  "Lanciano (Italie, an 700)",
  "Bolsena-Orvieto (Italie, 1263)",
  "Santarem (Portugal, 1247)",
  "Buenos Aires (Argentine, 1996)",
  "Tixtla (Mexique, 2006)",
  "Sokółka (Pologne, 2008)",
];

const miracleListDiv = document.getElementById("miracle-list");
if (miracleListDiv) {
  const ul = document.createElement("ul");
  miracles.forEach((m) => {
    const li = document.createElement("li");
    li.textContent = m;
    ul.appendChild(li);
  });
  miracleListDiv.appendChild(ul);
}

// === 🌙 GESTION DU MODE SOMBRE ===

// Création du bouton s’il n’existe pas déjà
let modeToggle = document.getElementById("mode-toggle");
if (!modeToggle) {
  modeToggle = document.createElement("button");
  modeToggle.id = "mode-toggle";
  modeToggle.textContent = "🌙 Mode sombre";
  document.querySelector("header").appendChild(modeToggle);
}

const body = document.body;

// Charger le mode préféré sauvegardé
if (localStorage.getItem("theme") === "dark") {
  body.classList.add("dark-mode");
  modeToggle.textContent = "☀️ Mode clair";
}

// Bouton toggle
modeToggle.addEventListener("click", () => {
  body.classList.toggle("dark-mode");

  if (body.classList.contains("dark-mode")) {
    modeToggle.textContent = "☀️ Mode clair";
    localStorage.setItem("theme", "dark");
  } else {
    modeToggle.textContent = "🌙 Mode sombre";
    localStorage.setItem("theme", "light");
  }
});
