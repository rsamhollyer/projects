import { URLs } from "../config.js";

const mainTag = document.querySelector("main");
let requestOptions = {
	method: "GET",
	redirect: "follow",
};

export const backgroundImage = () => {
	let randomGeneratedImageID = Math.floor(Math.random() * 201);
	fetch(`${URLs.backgroundImage}${randomGeneratedImageID}/info`, requestOptions)
		.then((response) => response.json())
		.then(
			(result) =>
				(mainTag.style.backgroundImage = `url(${result.download_url})`)
		)
		.catch((error) => console.log("Error", error));
};
