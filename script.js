 
const backToTop = document.createElement("button");
backToTop.id = "backToTop";
backToTop.textContent = "↑";
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


const elements = document.querySelectorAll("h2, h3, p, video");

function checkScroll() {
  const triggerBottom = window.innerHeight * 0.85;

  elements.forEach(el => {
    const rect = el.getBoundingClientRect();
    if (rect.top < triggerBottom) {
      el.classList.add("visible");
    }
  });
}

window.addEventListener("scroll", checkScroll);
checkScroll();

const miracles = [
  "Lanciano (Italie, an 700)",
  "Bolsena-Orvieto (Italie, 1263)",
  "Santarem (Portugal, 1247)",
  "Buenos Aires (Argentine, 1996)",
  "Tixtla (Mexique, 2006)",
  "Sokółka (Pologne, 2008)"
];

const miracleListDiv = document.getElementById("miracle-list");
if (miracleListDiv) {
  const ul = document.createElement("ul");
  miracles.forEach(m => {
    const li = document.createElement("li");
    li.textContent = m;
    ul.appendChild(li);
  });
  miracleListDiv.appendChild(ul);
}
