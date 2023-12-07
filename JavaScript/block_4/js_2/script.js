'use strict'

const form = document.getElementsByTagName('form')[0];

/*
<form action="https://api.tvmaze.com/search/shows">
    <input id="query" name="q" type="text">
    <input type="submit" value="Search">
</form>
</form>
*/

async function retriever(query) {
    const rawData = await fetch(`https://api.tvmaze.com/search/shows/?q=${query}`);
    const JSdata = await rawData.json();
    return JSdata;
}

form.addEventListener('submit', async function(event) {
    event.preventDefault();
    const search = document.getElementById('query').value;
    console.log(search);
    console.log(await retriever(search));
});