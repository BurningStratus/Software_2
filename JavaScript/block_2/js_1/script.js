/*
Write a program that prompts the user for five numbers and prints them in the reverse order they were entered. 

Print the result to the console.(2p)

    Save the numbers to an array, then use for-loop to iterate in reverse order.
    Do not use array.reverse() function.
*/

let integers = [];
let reverseInt = [];

for (let i = 1; i <= 5; i++) {
    const Integer = parseInt(prompt('Give integer:'));
    Integers.push(Integer);

}
console.log(integers);

for (i=0; -(i) < Integers.length; i--) {
    console.log(Integers[(Integers.length - 1) + i]);
}
console.log(reverseInt);
