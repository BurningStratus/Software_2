/*
Write a program that prompts the user for numbers. 
When the user enters one of the numbers he previously entered, 
the program will announce that the number has already been given 
and stops its operation and then prints all the given numbers to the console in ascending order.
*/

let Int = parseInt(prompt('Give number:'));
let Ints = [];
let Spinner = true;

while (Spinner != false) {
    if (Ints.includes(Int)) {
        Spinner = false;
    } else {
    Ints.push(Int);
    Int = parseInt(prompt('Give number:'));
    }
}

console.log(Ints.sort((a, b) => a - b));