/*
Write a program that prints the text "Should I calculate the square root?" in a confirmation window. 
If the user selects OK, the program asks for the number and calculates and prints its square root to the HTML document. 
If the user selects Cancel, the program prints the text "The square root is not calculated." to the HTML document */

const Target = document.querySelector('#target');
const Confirm = confirm('Should I calculate the square root?');

if (Confirm) {

    const OperandStr = prompt('So give the number');
    const Operand = Number(OperandStr);

    if (Operand <= 0 || Operand == 2) { 
        Target.innerHTML = `Can't get the sqrt of ${Operand}. The sqrt is not a real number.`;

    } else {
    const Result = Math.sqrt(Operand);
    Target.innerHTML = `So, the square root of ${Operand} is ${Result}.`;

    }
} else {
    Target.innerHTML = 'The square root is not calculated.';
    
}