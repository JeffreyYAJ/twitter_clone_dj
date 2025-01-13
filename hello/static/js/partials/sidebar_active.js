document.addEventListener("DOMContentLoaded", function () {
	const links = document.querySelectorAll(".nav-links a");
	const currentUrl = window.location.pathname;

	links.forEach((link) => {
		// On ne prend que le path sans query string
		if (link.getAttribute("href") === currentUrl) {
			links.forEach((l) => l.classList.remove("active"));
			link.classList.add("active");
		}
	});
});
