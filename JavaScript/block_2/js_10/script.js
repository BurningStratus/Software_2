/*
Write a voting program as described below for small-scale meeting use. (8p)

    The program asks for the number of candidates.
    Then the program asks for the names of the candidates: 'Name for candidate 1
    Store the candidates' names and initial vote count in objects like this:

[
    {
        name: 'ellie',
        votes: 0,
    },
    {
        name: 'frank',
        votes: 0,
    }, 
    {
        name: 'pamela',
        votes: 0,
    },
]

    The program asks for the number of voters.
    The program asks each voter in turn who they will vote for. Voter shoud enter candidate name. 
    If the voter enters an empty value instead of the voting number, it will be interpreted as an empty vote.
    The program announces the name of the winner and the results by printing it to the console:

The winner is pamela with 3 votes.
results:
pamela: 3 votes
frank: 1 votes
ellie: 1 votes

    Some help:

// You need to compare votes so console log a and b to see how to get the correct property.
someArray.sort((a, b) => {
   console.log(a, b);
   return b - a;
});
*/

let candidatesList = [];
const candidatesAmt = parseInt(prompt('Amount of candidates:'));

for (i = 0; i < candidatesAmt; i++) {
    const candName = prompt('Name of candidate:');
    candidatesList.push(
        {
        name: candName,
        vote: 0
        }
    )
}
for (i = 0; i < candidatesList.length; i++) {
    console.log(candidatesList[i]);
}

const votersAmt = parseInt(prompt('How many voters are there?'));
for (i = 0; i < votersAmt; i++) {
    const vote = prompt('Who are you voting for?(wrong answers only)')
    
    for (j = 0; j < candidatesList.length; j++) {
        if (vote == candidatesList[j]['name']); {
            candidatesList[j]['vote'] += 1;
            }
        }
    }
