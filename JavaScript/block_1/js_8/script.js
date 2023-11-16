/**
 * Write a program that prompts the user for the start and end year. 
 * The program prints all leap years from the interval given by the user. 
 * Printing is done in an unordered list to the HTML document. (3p)

    Example output HTML code:
<ul>
   <li>1992</li>
   <li>1996</li>
   <li>2000</li>
   <li>2004</li>
   <li>2008</li>
</ul>
 */


const Target = document.querySelector('#target');

const YearNotAbs = prompt('Define the start year');
const EndYearNotAbs = prompt('Define the end year');

let Year = Number(YearNotAbs);
let EndYear = Number(EndYearNotAbs);

let Leap = false;

for (let i = Year;  i <= EndYear; i++) { 
    
    if (i % 100 == 0 && i % 400 == 0) {
        Leap = true;
    } else if (i % 4 == 0 && i % 100 != 0) {
        Leap = true;
    } else {
        Leap = false;
    }

    if (Leap) {
        let YearStr = `${i}`;
        const Item = document.createElement('li');
        Item.innerText = YearStr;
        // DoListItem.createElement(li);
        Target.append(Item);
    }
    }

// bullet.innerHTML = `<b>${bullet.innerHTML}</b>`