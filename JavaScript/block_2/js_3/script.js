/*
Write a program that asks for the names of six dogs. 
The program prints dog names to unordered list <ul> 
in reverse alphabetical order
*/
const Target = document.querySelector('#target');
let DogsArray = [];

for (i = 0; i < 6; i++) {
    const Dog = prompt("Dog's name");
    DogsArray.push(Dog);
}

console.log(DogsArray);

DogsArray.sort();
DogsArray.reverse();

for (i = 0; i < 6; i++) {
    Item = document.createElement('li');
    Item.innerHTML = `${DogsArray[i]}`
    Target.append(Item);
}