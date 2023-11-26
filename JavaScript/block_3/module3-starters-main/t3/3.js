'use strict';
/*
Add HTML by using innerHTML property. (2p)

Add the following HTML code to the element with id="target". 
Add the values from 'names' array to the <li> elements in a for-loop.

<li>John</li>
<li>Paul</li>
<li>Jones</li>
*/
const names = ['John', 'Paul', 'Jones'];

const target = document.getElementById('target');

for (let i = 0; i < names.length; i++ ) {
    const name = names[i];
    const item = document.createElement('li');
    item.innerText = name;
    target.append(item);
} 

console.log('iteration ended.');