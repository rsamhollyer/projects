const main = document.querySelector("main");

export const generateAnImage = () => {
	const direction = Math.floor(Math.random() * 361); //this is to choose the direction of the gradient

	//This generates our two random RGBA colors - opacity is kept constant
	const red1 = Math.floor(Math.random() * 256);
	const green1 = Math.floor(Math.random() * 256);
	const blue1 = Math.floor(Math.random() * 256);
	const red2 = Math.floor(Math.random() * 256);
	const green2 = Math.floor(Math.random() * 256);
	const blue2 = Math.floor(Math.random() * 256);
	//Places the style on page load
	main.style.background = `linear-gradient(${direction}deg, rgba(${red1},${green1},${blue1}, .7), rgba(${red2},${green2},${blue2},.7))`;
};

generateAnImage();
