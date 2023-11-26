
// Browser Object Model

console.log(window);
// alert('Hi there');

console.log(window.document);

const confirmation = confirm('Are you sure?');
if (confirmation) {
    console.log('User selected OK');
} else {
    console.log('User selected Cancel');
}

const userInput = prompt('Write somthing');

const targetElement = document.querySelector('#funny');

function clickFunction(event) {
    console.log('click!');
    event.preventDefault();
    return
}

const htmlDoc = document.querySelector('html');

targetElement.addEventListener('click', function(event) {
    console.log('pressed', event.key);
});

let pressd = true;

targetElement.addEventListener('click', function(){
    htmlDoc.style = 'background-color: black';
});