
const body = document.body;
const button = document.createElement('button');
button.innerText = 'click';

xcom = button.addEventListener("keypress", function(event){
    console.log(event.key)
});

button.removeEventListener('keypress', button);

body.append(button);