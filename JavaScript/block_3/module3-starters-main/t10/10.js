/*
Read the first name and last name values from the form and print them in the <p id="target"> (2p)

remember to stop the default action of the form
you can use attribute selectors in querySelector() to select the <input> elements
example output: Your name is Luke Skywalker
*/

const readValues = document.getElementById('source');
const target = document.getElementById('target');

readValues.addEventListener('submit', function() {
    event.preventDefault();
    
    let firstname = document.querySelectorAll('input')[0].value;
    let lastname = document.querySelectorAll('input')[1].value;

    target.innerHTML = `Your name is ${firstname} ${lastname}.`;
});