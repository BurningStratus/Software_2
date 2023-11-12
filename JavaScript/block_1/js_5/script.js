/* 
Write a program that asks the user to enter a year and notifies the user whether the input year is a leap year. 

A year is a leap year if it is divisible by four. 
However, years divisible by 100 are leap years only if they are also divisible by 400. 

Print the result on the HTML document. (3p)
*/
const target = document.querySelector('#target0');

const YearNotAbs = Number(prompt("Enter the year to check if it is a leap one:"));
const Year = Math.abs(YearNotAbs);
let Leap;

if (Year % 100 == 0 && Year % 400 == 0) {
    Leap = 'is a leap year';
} else if (Year % 4 == 0 && Year % 100 != 0) {
    Leap = 'is a leap year';
} else {
    Leap = 'not a leap year';
}

target.innerHTML = `${Year} ${Leap}.`;
