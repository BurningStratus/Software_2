// Open APIs
// Block 4 || Geolocation Examples


// navigator.geolocation geolocation-finder API provided by browser
// callback functions
/*
function positionSuccess(position) {
    console.log('successful call', position);
    coordinates = position.coords;

    console.log('your position: ', 
    coordinates.latitude, 
    coordinates.longitude
    );

};
function positionError(error) {
    console.log('error on call', error);
};

navigator.geolocation.getCurrentPosition(
    positionSuccess, 
    positionError, 
    {enableHighAccuracy: true}
);

console.log('after geoloc call')
*/


// open APIs (Application Programming Interface)
// AJAX = Asynchronous JavaScript And XML


// oldschool handling of "promise"
const joke = fetch('https://api.chucknorris.io/jokess/random').then(
    function (response) {
        console.log('successful call:> ' + response);

    }).catch(
    function (error) {
        console.log('error on call:> ' + error);

    }
);
// modern way of handling "promise"
async function fetchJoke() {
    let jokeContent;

    try {
        const response = await fetch('https://api.chucknorris.io/jokes/random');
        const newJoke = await response.json();
        console.log(newJoke);
        const target = document.getElementById('target0');
        target.innerText = newJoke['value'];
    } catch(error) {
        console.log('no joke today :( ', error);
        const joke = {};
        jokeContent = 'no jokes for you :(';
    }
}
fetchJoke();
