

const Target = document.querySelector('#target');
let CastedDice = [];
let Dice = 0;

function DiceCaster(DiceAmt) {
    return Math.floor(Math.random() * DiceAmt + 1);
}

const DiceSidesAmt = parseInt(prompt('How many sides does your dice have?'))

while (Dice != DiceSidesAmt) {
    Dice = DiceCaster(DiceSidesAmt);
    CastedDice.push(Dice);

    Item = document.createElement('li');
    Item.innerHTML = String(Dice);
    Target.append(Item);
} 
console.log(CastedDice);
console.log(`it took [${CastedDice.length}] casts to get ${DiceSidesAmt}.`);
