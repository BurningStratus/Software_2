'use strict';

/*
Add HTML by using createElement() and appenChild mehtods. (2p)

Add the following HTML code to the element with id="target". 
Add the values from 'students' array to the <option> elements in a for-loop.

<option value="2345768">John</option>
<option value="2134657">Paul</option>
<option value="5423679">Jones</option>
*/

const element = document.getElementById('target');
const students = [
  {
    name: 'John',
    id: '2345768',
  },
  {
    name: 'Paul',
    id: '2134657',
  },
  {
    name: 'Jones',
    id: '5423679',
  },
];

for (let i = 0; i < students.length; i++) {
  const item = document.createElement('option');
  item.value = students[i]["id"];
  item.innerHTML = students[i]["name"];
  element.appendChild(item);
};