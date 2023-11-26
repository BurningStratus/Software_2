/*
This is continuation to previous task. 
There is only one text field left, where the user writes 
the calculation (addition, subtraction, multiplication or division)

    You can use the includes and split methods.
    eval() function is prohibited
    No need to support decimal numbers, calculating integers is enough.
    Example inputs: 3+5, 2-78, 3/6, etc..
*/

'use strict';

let target = document.getElementById('result');
let trigger = document.getElementById('start');

function Meth() {
    
    let rawExpression = document.getElementById('calculation').value;
    let x, y;
    let result;

    if (rawExpression.includes('+')) {
        x = rawExpression.split('+')[0];
        y = rawExpression.split('+')[1];
        result = parseInt(x) + parseInt(y);

    } else if (rawExpression.includes('*')) {
        x = rawExpression.split('*')[0];
        y = rawExpression.split('*')[1];
        result = parseInt(x) * parseInt(y);
    
    } else if (rawExpression.includes('/')) {
        x = rawExpression.split('/')[0];
        y = rawExpression.split('/')[1];
        result = parseInt(x) / parseInt(y);

    } else if (rawExpression.includes('-')) {
        if (rawExpression[0] == '-') {
            x = parseInt(rawExpression.split('-')[1]);
            y = parseInt(rawExpression.split('-')[2]);
            result = - x - y;

        } else {
            x = rawExpression.split('-')[0];
            y = rawExpression.split('-')[1];
            result = parseInt(x) - parseInt(y);
        }

    } else {
        console.log('not work');
    }
    return result;
}

trigger.addEventListener('click', function (){
    let result = Meth();
    console.log(result);
    target.innerHTML = result;
});

