// console.log(fetch('http://127.0.0.1:3000/add/1/2'));
const target = document.getElementById("fun");
async function deAdd() {
    let num1 = parseInt(prompt('num1'));
    let num2 = parseInt(prompt('num2'));

    const response = await fetch(`http://127.0.0.1:3000/add/${num1}/${num2}`);
    const responseJSON = await response.json();
    console.log(responseJSON);
    target.innerText = responseJSON.sum;
}

deAdd();