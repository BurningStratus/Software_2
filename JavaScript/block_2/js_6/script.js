/**
 * Write a function that returns a random dice roll between 1 and 6. 
 * The function should not have any parameters. 
 * 
 * Write a main program that rolls the dice until the result is 6. 
 * The main program should print out the result of each roll in an unordered list (<ul>)
 */

const Target = document.querySelector('#target');
let CastedDice = [];
let Dice = 0;

function DiceCaster() {
    const Caster = Math.floor(Math.random() * 6 + 1);
    return Caster;
}

while (Dice != 6) {
    Dice = DiceCaster();
    CastedDice.push(Dice);
    console.log(Dice);

    Item = document.createElement('li');
    Item.innerHTML = String(Dice);
    Target.append(Item);
} 
console.log(`it took [${CastedDice.length}] casts to get 6.`)
