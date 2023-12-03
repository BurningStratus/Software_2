'use strict'

const form = document.getElementsByTagName('form')[0];

/*
Develop the app even further. Optional chaining is not the best way to handle missing image. 
Use ternary operator or if/else to add a default image if TV-show is missing image property.
    Use https://via.placeholder.com/210x295?text=Not%20Found as the default image.
*/

async function retriever(query) {
    const rawData = await fetch(`https://api.tvmaze.com/search/shows/?q=${query}`);
    const JSdata = await rawData.json();
    return JSdata;
}
async function getDefault() {
    await fetch("https://via.placeholder.com/210x295?text=Not%20Found", {
    method: 'GET',
    mode: 'no-cors' 
    }).then()
}

function showData(objectData) {
    // creating elements
    let data = objectData.show;
    const header2 = document.createElement('h2');
    header2.innerText = data.name;

    const seriesUrl = document.createElement('a');
    seriesUrl.href = data.url;
    seriesUrl.target = "_blank";
    seriesUrl.innerText = `Link to ${data.name} page on TVMaze`;

    const poster = document.createElement('img');
    // check if there is a poster for the show
    if (data.image?.medium === undefined) {
        console.log("couldn't find the picture.\nusing the default one instead.");
        poster.src = "https://via.placeholder.com/210x295?text=Not%20Found";
        // 
    } else {
        console.log('found the picture!');
        poster.src = data.image.medium;

    }
    poster.alt = data.name;

    const summary = document.createElement('div');
    summary.innerHTML = data.summary;

    // adding them to the article
    const article = document.createElement('article');
    article.classList.add('article');
    article.append(header2, seriesUrl, poster, summary);
    return article;
}

form.addEventListener('submit', async function(event) {
    event.preventDefault();

    // clearing the element
    const main = document.querySelector('main')
    main.innerHTML = '';

    const search = document.getElementById('query').value;
    const objectShow = await retriever(search);

    console.log('constructing the page... ' + search);
    for (let i = 0; i < objectShow.length; i++) {
        ;
        let newArticle = showData(objectShow[i]);
        main.append(newArticle);
    }
    console.log('construction finished');
});