/*
Write a program that asks the user for the number of participants. 
After this, the program asks for the names of all participants. 

Finally, the program prints the names of the participants on the web page 
in an ordered list (<ol>) in alphabetical order.
*/
const Target = document.querySelector('#target');

const ParticipantsAmt = parseInt(prompt('How many participants?'));
let ParticipantsArray = []; 

for (i = 0; i < ParticipantsAmt; i++) {
    const Participant = prompt('Name:');
    ParticipantsArray.push(Participant);

}
ParticipantsArray.sort();

for (i = 0; i < ParticipantsAmt; i++) {
    ItemOL = document.createElement('li');
    ItemOL.innerHTML = `${ParticipantsArray[i]}`;
    Target.append(ItemOL);
}