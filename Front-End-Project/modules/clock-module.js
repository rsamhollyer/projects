// Variables to grab classes
const analogClock = document.querySelector(".analog-clock");
const analogClockFace = document.querySelector(".clock-face");
let secondHand = document.querySelector(".second-hand");
let minuteHand = document.querySelector(".minute-hand");
let hourHand = document.querySelector(".hour-hand");
let digitalClock = document.querySelector(".digital-clock");

export const runClock = () => {
	let now = new Date();
	let seconds = now.getSeconds();
	let minutes = now.getMinutes();
	let hours = now.getHours();

	if (!analogClock.classList.contains("hidden")) {
		let secondsPercent = seconds / 60;
		let minutesPercent = (secondsPercent + minutes) / 60;
		let hoursPercent = (minutesPercent + hours) / 12;

		rotateHands(secondHand, secondsPercent);
		rotateHands(minuteHand, minutesPercent);
		rotateHands(hourHand, hoursPercent);
	}

	if (!digitalClock.classList.contains("hidden")) {
		hours = hours < 10 ? `0${hours}` : `${hours}`;
		minutes = minutes < 10 ? `0${minutes}` : `${minutes}`;
		seconds = seconds < 10 ? `0${seconds}` : `${seconds}`;
		let am_pm = "AM";
		if (hours > 11) {
			am_pm = "PM";
		}

		if (hours > 12) {
			hours -= 12;
		}

		if (hours === 0) {
			hours = 12;
			am_pm = "AM";
		}
		let displayCurrentTime = `${hours} : ${minutes} : ${seconds} ${am_pm}`;
		digitalClock.innerText = displayCurrentTime;
	}
};

const rotateHands = (element, rotate) => {
	element.style.setProperty(`--rotation`, rotate * 360);
};
