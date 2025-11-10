// ========================
// 📌 Navigation pour saints
// ========================
const saints = [
  { name: "Carlo Acutis", url: "carlo.html" },
  { name: "Pier Giorgio Frassati", url: "giorgio.html" },
  { name: "Padre Pio", url: "padrepio.html" },
  { name: "Saint Tarcisius", url: "tarcisius.html" },
  { name: "Saint Augustin", url: "augustin.html" },
  { name: "Sainte Thérèse de Lisieux", url: "therese.html" },
  { name: "Sainte Rita de Cascia", url: "rita.html" },
  { name: "Charbel Makhlouf", url: "charbel.html" },
];

function generateSaintsNav() {
  const saintsNav = document.querySelector(".saints-nav ul");
  if (!saintsNav) return;

  saintsNav.innerHTML = saints
    .map((saint) => `<li><a href="${saint.url}">${saint.name}</a></li>`)
    .join("");
}

generateSaintsNav();

// ========================
// 📌 Citation aléatoire
// ========================
const quotes = [
  "« L’Eucharistie est mon autoroute vers le ciel. » - Carlo Acutis",
  "« Verso l’alto ! » (Toujours plus haut) - Pier Giorgio Frassati",
  "« Prie, espère et ne t’inquiète pas. » - Padre Pio",
  "« Un chrétien ne doit jamais avoir peur de témoigner. » - Tarcisius",
  "« Nos cœurs sont sans repos tant qu’ils ne reposent en Toi. » - Saint Augustin",
  "« Je passerai mon ciel à faire du bien sur la terre. » - Thérèse de Lisieux",
  "« Là où il n’y a pas d’amour, mettez de l’amour. » - Sainte Rita",
];

function showRandomQuote() {
  const quoteBox = document.getElementById("quote");
  if (!quoteBox) return;

  const randomIndex = Math.floor(Math.random() * quotes.length);
  quoteBox.textContent = quotes[randomIndex];
}

showRandomQuote();

// ========================
// 📌 Bouton "Retour en haut"
// ========================
const btnTop = document.createElement("button");
btnTop.id = "btnTop";
btnTop.textContent = "⬆ Haut";
document.body.appendChild(btnTop);

// Style via CSS pour rester cohérent
btnTop.style.cssText = `
  position: fixed;
  bottom: 30px;
  right: 30px;
  background-color: var(--accent-color);
  color: #000;
  border: none;
  padding: 10px 15px;
  border-radius: 8px;
  cursor: pointer;
  font-weight: bold;
  box-shadow: 0 4px 10px var(--shadow-color);
  opacity: 0;
  pointer-events: none;
  transition: opacity 0.3s;
`;

window.addEventListener("scroll", () => {
  if (window.scrollY > 200) {
    btnTop.style.opacity = "1";
    btnTop.style.pointerEvents = "auto";
  } else {
    btnTop.style.opacity = "0";
    btnTop.style.pointerEvents = "none";
  }
});

btnTop.addEventListener("click", () => {
  window.scrollTo({ top: 0, behavior: "smooth" });
});
