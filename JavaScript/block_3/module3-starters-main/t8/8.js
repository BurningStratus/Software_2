/* 
Make a simple calculator. (4p)

There are two input fields where user enters numbers.

Based on the drop-down list, calculator performs 
addition, subtraction, multiplication or division 
of these two numbers.

Use the value attribute of <option> elements to 
decide which operation the calculator needs to do. Example:
Show the result in <p id="result"> when the button is clicked.
*/
const triggerNode = document.getElementById('start');
const resultNode = document.getElementById('result');

triggerNode.addEventListener('click', function() {
    console.log('func started');
    const functional = document.getElementById('operation').value;
    const int1 = parseInt(document.getElementById('num1').value);
    const int2 = parseInt(document.getElementById('num2').value);
    
    let result;
    console.log(functional);

    switch (functional) {
        case 'add':
            result = int1 + int2;
            break;
        case 'sub':
            result = int1 - int2;
            break;
        case 'multi':
            result = int1 * int2;
            break;
        case 'div':
            result = int1 / int2;
            break;
    }
    console.log(result);
    resultNode.innerText = result;
});