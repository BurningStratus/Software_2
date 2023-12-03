'use strict'

const form = document.getElementsByTagName('form')[0];

/*
Develop the app even further. Print the following information for all series 
from the search result on the web page.

:: required information: Name, link to details (url), medium image and summary
:: show the name in <h2> element
:: show the url in <a> element. Also add target="_blank" to the link.
:: show the medium image with <img src="" alt="">. 
:  Add medium image to src attribute and name property to alt attribute.

:: some TV-shows don't have images. This will cause an error. 
:  You can fix this by adding ? operator to image property. 
:  Example: tvShow.show.image?.medium;. This is called optional chaining.

:: show summary in <div> element (not <p>).
:  This is because the summary is already in <p> element, 
:  and the result will not be valid if <p> is inside another <p>.

:: collect the elements to <article> elements and 
:  append <article> elements to the HTML document.
:  make <div id="results"> element to the HTML document 
:  where you append the <article> elements.

:: clear the old results with innerHTML = '' before you append the new results.
*/

async function retriever(query) {
    const rawData = await fetch(`https://api.tvmaze.com/search/shows/?q=${query}`);
    const JSdata = await rawData.json();
    return JSdata;
}

function showData(objectData) {
    // creating elements
    let data = objectData.show;
    const header2 = document.createElement('h2');
    header2.innerText = data.name;

    const seriesUrl = document.createElement('a');
    seriesUrl.href = data.url + "_blank";
    seriesUrl.innerText = `Link to ${data.name} page on TVMaze`

    const poster = document.createElement('img');
    poster.src = data.image?.medium;
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