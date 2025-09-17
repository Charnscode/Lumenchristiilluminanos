
// Navigation dynamique

const saints = [
  { name: "Carlo Acutis", url: "carlo.html" },
  { name: "Pier Giorgio Frassati", url: "giorgio.html" },
  { name: "Padre Pio", url: "padrepio.html" },
  { name: "Saint Tarcisius", url: "tarcisius.html" },
  { name: "Saint Augustin", url: "augustin.html" },
  { name: "Sainte Thérèse de Lisieux", url: "therese.html" },
  { name: "Sainte Rita de Cascia", url: "rita.html" },
  { name: "Saint Charbel MAKHLOUF", url: "charbel.html" }
];

// Générer un menu automatiquement
function generateMenu() {
  const nav = document.querySelector("nav");
  if (!nav) return;

  nav.innerHTML = saints.map(saint => 
    `<a href="${saint.url}">${saint.name}</a>`
  ).join(" | ");
}

generateMenu();



//  Citation aléatoire

const quotes = [
  "« L’Eucharistie est mon autoroute vers le ciel. » - Carlo Acutis",
  "« Verso l’alto ! » (Toujours plus haut) - Pier Giorgio Frassati",
  "« Prie, espère et ne t’inquiète pas. » - Padre Pio",
  "« Un chrétien ne doit jamais avoir peur de témoigner. » - Tarcisius",
  "« Nos cœurs sont sans repos tant qu’ils ne reposent en Toi. » - Saint Augustin",
  "« Je passerai mon ciel à faire du bien sur la terre. » - Thérèse de Lisieux",
  "« Là où il n’y a pas d’amour, mettez de l’amour. » - Sainte Rita"
];

function showRandomQuote() {
  const quoteBox = document.getElementById("quote");
  if (!quoteBox) return;

  const randomIndex = Math.floor(Math.random() * quotes.length);
  quoteBox.textContent = quotes[randomIndex];
}

showRandomQuote();


// ========================
// 📌 Bouton retour en haut
// ========================
const btnTop = document.createElement("button");
btnTop.textContent = "⬆ Haut";
btnTop.id = "btnTop";
document.body.appendChild(btnTop);

btnTop.style.display = "none";

window.addEventListener("scroll", () => {
  if (window.scrollY > 200) {
    btnTop.style.display = "block";
  } else {
    btnTop.style.display = "none";
  }
});

btnTop.addEventListener("click", () => {
  window.scrollTo({ top: 0, behavior: "smooth" });
});



// Effet de fondu sur le fond

document.body.style.transition = "background 1.5s ease-in-out";