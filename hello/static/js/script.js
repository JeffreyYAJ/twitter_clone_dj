document.addEventListener("DOMContentLoaded", function () {
	document.querySelectorAll(".like-btn").forEach(function (btn) {
		btn.addEventListener("click", function () {
			// Example: Toggle like button color
			btn.classList.toggle("liked");
		});
	});
});
