var hamburger = document.querySelector(".hamburger");
var nav = document.querySelector(".navMenu");

hamburger.addEventListener("click", () => {
	if (nav.classList.contains("show")) {
		nav.classList.remove("show");
	} else {
		nav.classList.add("show");
	}
});

const searchicon = document.getElementById("searchbtn");
const searchMenu = document.getElementById("searchMenu");
const searchtoggle = document.querySelector("[data-action='search-toggle']");
const searchClose = document.querySelector(".search-close");

searchtoggle.addEventListener("click", () => {
	if (searchMenu.classList.contains("show")) {
		searchMenu.classList.remove("show");
	} else {
		searchMenu.classList.add("show");
	}
});

searchClose.addEventListener("click", () => {
	searchMenu.classList.remove("show");
});
