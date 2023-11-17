/*
Write a program that asks the user for numbers until he gives zero. 
The given numbers are printed in the console from the largest to the smallest.
*/

let Integers = [];

do {
    Int = parseInt(prompt('Integer:'));
    Integers.push(Int);
    
} while (Int != 0);

Integers.sort((prev, next) => next - prev);
console.log(Integers);