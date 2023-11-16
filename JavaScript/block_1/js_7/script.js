/*
Write a program that rolls user defined number of dice and displays the sum of the results of the dice rolls.(2p)
    First, program asks the user for the number of dice rolls.
    Then the program throws a die as many times as the user defined.
    Print the sum of the results in the console or in the HTML document.
*/

const Target = document.querySelector('#target');
const RollsStr = prompt('How many dice whall we roll?');
const Rolls = Number(RollsStr);
let Results = 0;
let Faces = [];


for (i = 1; i <= Rolls; i++) {
    const Dice = Math.floor(Math.random() * 6) + 1;
    Results = Dice + Results;
    Faces.push(Dice);
}
Target.innerHTML = `${Rolls} Were thrown[${Faces}]. Sum of all results is ${Results}.`;