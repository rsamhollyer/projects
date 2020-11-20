import { URLs } from "./../config.js";
let requestOptions = {
	method: "GET",
	redirect: "follow",
};

const quoteSection = document.querySelector(".quote-section");
const refreshButton = document.querySelector(".refresh-quote");
export const newQuote = () => {
	fetch(URLs.quote, requestOptions)
		.then((response) => response.json())
		.then((result) => {
			let { quoteText, quoteAuthor } = result.quote;
			appendQuoteToDOM(quoteText, quoteAuthor);
		});
};

//This function handles all the DOM heaving lifting
const appendQuoteToDOM = (quote, author) => {
	const paragraph = document.querySelector("#quote-paragraph");
	const authorNameId = document.querySelector("#author-name");
	refreshButton.disabled = false;
	//This logic runs the display text of the quote that is generated. It returns out to stop running the code below since that only needs to be run the first time the AJAX is run

	if (paragraph) {
		paragraph.innerText = quote;
		authorNameId.innerText = author || "-unknown";
		return;
	}
	let div = document.createElement("div");
	let p = document.createElement("p");
	p.id = "quote-paragraph";
	p.append(quote);
	div.append(p);
	quoteSection.prepend(div);

	let authorEL = document.createElement("h6");
	authorEL.id = "author-name";

	//Need to make sure to account for any missing author value from the JSON
	if (author != false) {
		authorEL.append(author);
		div.append(authorEL);
	} else {
		authorEL.append("-unknown");
		div.append(authorEL);
	}
};
