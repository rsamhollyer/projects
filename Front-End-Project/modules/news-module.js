import { URLs } from "../config.js";

let requestOptions = {
	method: "GET",
	redirect: "follow",
};

export const newsUpdate = () => {
	fetch(URLs.news, requestOptions)
		.then((response) => response.json())
		.then((result) => placeNewsOnPage(result))
		.catch((error) => console.log("error", error));
};

const placeNewsOnPage = (res) => {
	res.articles.forEach(makeArticle);
};

const makeArticle = (article) => {
	let newsContainer = document.querySelector(".container");

	let newsList = document.createElement("ol");
	let newsItems = document.createElement("li");
	let newsTitle = document.createElement("div");
	newsTitle.classList = "article-title";

	let imgDiv = document.createElement("div");
	imgDiv.classList = "center-img";

	let newsImg = document.createElement("img");
	newsImg.src = article.urlToImage;
	newsImg.classList = "news-img";

	let newsDescription = document.createElement("p");
	newsDescription.classList = "description";

	let newsAnchor = document.createElement("a");
	newsAnchor.classList = "anchor";
	newsAnchor.href = article.url;
	newsAnchor.innerText = "Read More";
	newsAnchor.target = "_blank";

	newsTitle.append(article.title);
	newsDescription.append(article.description);
	newsItems.append(newsTitle);
	newsItems.append(imgDiv);
	imgDiv.append(newsImg);
	newsItems.append(newsDescription);
	newsItems.append(newsAnchor);
	newsList.append(newsItems);
	newsContainer.append(newsList);
}
