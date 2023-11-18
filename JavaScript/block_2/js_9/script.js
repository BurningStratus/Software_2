/*
Write a function called even(), which receives an array containing numbers as a parameter. 
The function returns a second (usually smaller) array which has the even numbers of the original array. 
The function must not make changes to the original table. (3p)

    Example: In a three-item array, there are items 2, 7 and 4. The function returns a two-item array with items 2 and 4.
    Print both the original array and the new array to the console in the main program after you have called the function.
    You can hard code the array, no need for prompt()
*/

const UnevenArray = [1, 4, 5, 15, 13, 17, -1, 6, 7];

function even(unevenArray) {
    let evenArray = [];
    for (i = 0; i < unevenArray.length; i++) {
        if (unevenArray[i] % 2 == 0) {
            evenArray.push(unevenArray[i]);
        }
    }
    return evenArray;
}
const EvenArray = even(UnevenArray);

console.log(UnevenArray);
console.log(EvenArray);