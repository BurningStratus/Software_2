
const button = window.document.getElementById('butt');

button.innerText = 'DO NOT CLICK!!!';
button.addEventListener('click', () => {
    console.log(Math.floor(Math.random() + 1));
})

let target = document.getElementById('target0');
let documentWhole = document.getElementsByTagName('html')[0];

documentWhole.addEventListener('contextmenu', (event) => {
    event.preventDefault();
    console.log('no right click :)')
})

documentWhole.addEventListener('keydown', (event) => {
    documentWhole = document.getElementsByTagName('html')[0];

    if (event.key == 'F12') {
        event.preventDefault();
        target.innerHTML = 'no';
    }
})

const list = [1, 2, 3];

console.log(length.list)