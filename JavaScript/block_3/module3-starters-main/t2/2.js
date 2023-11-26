/*
Add HTML by using createElement() and appenChild methods. (2p)

    Add the following HTML code to the element with id="target"

<li>First item</li>
<li>Second item</li>
<li>Third item</li>

Add class my-item to the second list item
*/
const target = document.getElementById('target')

Item1 = document.createElement('li');
Item2 = document.createElement('li');
Item3 = document.createElement('li');

Item1.innerHTML = '<li>First item</li>';
Item2.innerHTML = '<li>Second item</li>';
Item3.innerHTML = '<li>Third item</li>';

target.appendChild(Item1);
target.appendChild(Item2);
target.appendChild(Item3);

Item2.classList.add('my-item');