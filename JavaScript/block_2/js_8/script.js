const Target = document.querySelector('#target0');
/*
Write a function called concat(), which receives an array of strings as a parameter. 
The function returns a string formed by concatenating the elements of the array. (2p)

    Example: In a four-item array, there are items Johnny, DeeDee, Joey and Marky. 
    The function returns the string JohnnyDeeDeeJoeyMarky.

    Do not use array.join() function
    You can hardcode the array, no need for prompt().
    Print the result to HTML document.

*/
function concat(array) {
    let concatStr = '';
    for (i = 0; i < array.length; i++) {
        console.log(array[i])
        concatStr = concatStr + array[i];
    }
    return concatStr;
}

const Names = ['Dino','Dean','Jack','Quebec'];
const ConcatNames = concat(Names);

console.log(ConcatNames);

Target.innerHTML = ConcatNames;