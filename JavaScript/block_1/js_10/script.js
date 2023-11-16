Target = document.querySelector('#target');

/*
Make a program that asks the user for the number of dice and the sum of the eye numbers of interest to the user. 
The purpose of your program is now to find out with what probability the number of dice 
given by the user produces the sum of the number of eyes given by the user. 

For example, if the user enters 3 as the number of dice and 17 as the sum of the eyes, 
the program calculates the probability that the sum of the three dice's eye numbers is 17

    Solve the problem by simulating: Have the program roll a given number of dice in a for-loop (e.g. 10,000 times) 
    and calculate what proportion of the repetitions produced the sum of eye numbers of interest to the user.
    
    Print the result on the HTML document:

Probability to get sum 7 with 2 dice is 15.64%

    you can limit the number of decimals with toFixed()
    test values:
        2 dice, sum 7, probability is about 15-17%
        3 dice, sum 15, probability is about 5%

*/

const Dice = parseInt(prompt('How many dice shall we throw?'));
const DesiredSum = parseInt(prompt('Which sum to look for?'));
const AllThrows = 100000;
let DesiredThrows = 0;

for (t = 0; t <= AllThrows; t++) {
    let Dice_1 = Math.floor(Math.random() * 6);
    let Dice_2 = Math.floor(Math.random() * 6);
    let Dice_3 = Math.floor(Math.random() * 6);

    if (Dice_1 + Dice_2 + Dice_3 == DesiredSum) {
        DesiredThrows += 1;
    }
}
if (DesiredThrows == 0) {
    DesiredThrows = 1;
}
const ProbabilityLong = DesiredThrows / AllThrows;
const Probability = ProbabilityLong.toFixed(4) * 100;

Target.innerHTML = `Dice [${Dice} pieces] were cast ${AllThrows} times. The probability to get the sum of ${DesiredSum} is ~ ${Probability}%.`;