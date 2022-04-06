var modalBtn = document.querySelector(".modal-btn");
var modalBg = document.querySelector(".modal-bg");
var modalClose = document.querySelector(".modal-close");

modalBtn.addEventListener("click", function () {
	modalBg.classList.add("bg-active");
});

modalClose.addEventListener("click", () => {
	modalBg.classList.remove("bg-active");
});
