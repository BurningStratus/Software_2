const Target = document.querySelector('#target');
/*
Write a program that asks the user for an integer and tells if the number is a prime number. (2p)

    Prime numbers are numbers that are only divisible by 1 and itself.
    For example, number 13 is a prime number as it can only be divided by 1 or 13 so that the result is an integer.
    On the other hand, number 21 for example is not a prime number as it can be also be divided by numbers 3 and 7.
    Print the result on the HTML document.

*/

const Num = parseInt(prompt('Enter num to check if it is a prime number'));
let IsPrime = Boolean;

for (i = 0; i <= Num; i++) {
    if (Num % i == 0 && i != 1 && i != Num) {
        IsPrime = false;
    }
}

if (IsPrime) {
    Target.innerHTML = `${Num} is a prime number`;
} else {
    Target.innerHTML = `${Num} is not a prime number`;
}