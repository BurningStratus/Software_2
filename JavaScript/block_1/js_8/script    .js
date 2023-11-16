Year = 100;
EndYear = 200;
let Leap = false;

for (Year;  Year < EndYear; Year++) { 
    

    if (Year % 100 == 0 && Year % 400 == 0) {
        Leap = true;
    } else if (Year % 4 == 0 && Year % 100 != 0) {
        Leap = true;
    } else {
        Leap = false;
    }
}
console.log(Year, Leap);
