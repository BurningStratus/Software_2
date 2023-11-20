/*
Write a voting program as described below for small-scale meeting use. (8p)
    The program asks for the number of candidates.
    Then the program asks for the names of the candidates: 'Name for candidate 1
    Store the candidates' names and initial vote count in objects.

    The program asks for the number of voters.
    The program asks each voter in turn who they will vote for. Voter shoud enter candidate name. 
    If the voter enters an empty value instead of the voting number, it will be interpreted as an empty vote.
    The program announces the name of the winner and the results by printing it to the console:

The winner is pamela with 3 votes.
results:
pamela: 3 votes
frank: 1 votes
ellie: 1 votes
*/

let candidatesList = [];
const candidatesAmt = parseInt(prompt('Amount of candidates:'));

for (i = 0; i < candidatesAmt; i++) {
    const candName = prompt(`Name of candidate [${i + 1}/${candidatesAmt}]:`);

    candidatesList.push(
        {
        name: candName,
        votes: 0,
        serialNumber: i + 1
        }
    )
}
console.log(candidatesList);
const votersAmt = parseInt(prompt('How many voters are there?'));

for (i = 0; i < votersAmt; i++) {
    
    let vote = prompt(`Voter [${i + 1}/${votersAmt}], who are you voting for?\n` +
    '(type either the name of candidate or their serial number)');

    for (let j = 0; j < candidatesList.length; j++) {

        if (isNaN(parseInt(vote)) == true && vote == candidatesList[j]['name']) {
            candidatesList[j]['votes'] += 1;
    
            console.log('vote added');
            j = candidatesList.length;

        } else if (parseInt(vote) == candidatesList[j]['serialNumber']) {
                candidatesList[j]['votes'] += 1;
                
                console.log('vote added');
                j = candidatesList.length;

        //    console.log('not a numeber', isNaN(parseInt(vote)), vote, candidatesList[j]['name']);
        //    console.log('number', parseInt(vote), vote, candidatesList[j]['serialNumber'])
        }
    }
}

candidatesList.sort((a, b) => b.votes - a.votes);

console.log(`The winner is ${candidatesList[0]['name']} with ${candidatesList[0]['votes']} votes.\nresults:`);

for (i = 0; i < candidatesAmt; i++) {
    console.log(`${candidatesList[i]['name']}: ${candidatesList[i]['votes']} votes.`)
}
