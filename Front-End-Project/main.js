import { runClock } from "./modules/clock-module.js";
import { generateAnImage } from "./modules/gradient-module.js";
import { backgroundImage } from "./modules/background-image-module.js";
import { newQuote } from "./modules/quote.js";
import { newsUpdate } from "./modules/news-module.js";

const toggleWhichClock = document.querySelector(".toggle-switch");
const analogClock = document.querySelector(".analog-clock");
const digitalClock = document.querySelector(".digital-clock");
const refreshButton = document.querySelector(".refresh-quote");
const windowsScreenSize = window.matchMedia("(min-width:766px)");
const toggleLabel = document.querySelector(".toggle-label");

setInterval(runClock, 1000);
newQuote();
newsUpdate();

if (windowsScreenSize.matches) {
	backgroundImage();
} else {
	generateAnImage();
}

toggleWhichClock.addEventListener("change", () => {
	analogClock.classList.toggle("hidden");
	digitalClock.classList.toggle("hidden");
	if (analogClock.classList.contains("hidden")) {
		toggleLabel.innerText = `DIGITAL`;
	} else {
		toggleLabel.innerText = `ANALOG`;
	}
});

const handleScreenSize = (e) => {
	if (e.matches) {
		backgroundImage();
	}
	generateAnImage();
};

refreshButton.addEventListener("click", () => {
	refreshButton.disabled = true;
	newQuote();
});
windowsScreenSize.addListener(handleScreenSize); //Want to only run the background image AJAX when the screen is at or above 766px. Below that and we only run the gradient background color function
