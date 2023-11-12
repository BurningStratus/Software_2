/*
const name = prompt("insert: ");

console.log(name);

const merkkijono = "ur name is " + name;
console.log(merkkijono);

const styled = `hi there, ${name}`;
console.log(styled);

// DONT DO THIS!!! --->
// hoistproblem will arise!(use before definition)
let age = 13;

console.log(age);

// that's why we use strict mode and let/const

let first_name = "Big";
let last_name;

last_name = "Lebowski";

first_name = first_name + ' ' + last_name;
console.log(first_name);

let sec_name = 'Benjamin';
let lasted_name = 'Franklin';


sec_name = sec_name + ' ' + lasted_name;
*/
/*
const table = [1, 2, 3, 4, 5, 6];

console.log(table);

table[0] = 20;

console.log(table);

let name = 'Tatra';
console.log(typeof name, name);

name = 200;
console.log(typeof name, name);

let ageStr = "13";
console.log(ageStr);

let age = ageStr.toString();

*/

const htmlName = 'lorem';
const element = document.querySelector('#text');
element.innerHTML = `Hi, ${htmlName}`;
element.computedStyleMap.color = 'red';

