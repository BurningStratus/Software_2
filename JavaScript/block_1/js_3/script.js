
// sum, product, avg of three ints

const target1 = document.querySelector('#target1');
const target2 = document.querySelector('#target2');
const target3 = document.querySelector('#target3');

const Num1 = prompt('enter first integer:');
const Num2 = prompt('enter second integer:');
const Num3 = prompt('enter third integer:');

const IntNum1 = Number(Num1);
const IntNum2 = Number(Num2);
const IntNum3 = Number(Num3);

const Sum = IntNum1 + IntNum2 + IntNum3;
const Prod = IntNum1 * IntNum2 * IntNum3;
const Avg = Sum / 3;

target1.innerHTML = `Sum of ${Num1}, ${Num2}, ${Num3} is ${Sum}.`;
target2.innerHTML = `Product of ${Num1}, ${Num2}, ${Num3} is ${Prod}.`;
target3.innerHTML = `Average of ${Num1}, ${Num2}, ${Num3} is ${Avg}.`;

