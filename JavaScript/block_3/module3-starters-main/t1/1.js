/**
 * Open t1 folder in your IDE/editor. Add HTML by using innerHTML property (2p)

    Add the following HTML code to the element with id="target"

<li>First item</li>
<li>Second item</li>
<li>Third item</li>

Add class my-list to the element with id="target"
 */

const Target = document.getElementById('target');
const unList = document.querySelector('ul');

Items = `<li>First item</li>
         <li>Second item</li>
         <li>Third item</li>`;

Target.innerHTML = Items;

unList.classList.add("my-list");