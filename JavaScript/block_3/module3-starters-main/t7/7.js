'use strict';

/* 
Make a hover effect with JavaScript. (2p)

when user mouses over <p id="trigger"> 
change the picture of <img id="target"> form picA.jpg to picB.jpg
when user mouses off, change the picture back to origin
*/

const trigger = document.getElementById('trigger');
const target = document.getElementById('target');

trigger.addEventListener('mouseover', () => {
    target.src = 'img/picB.jpg';
});
trigger.addEventListener('mouseleave', () => {
    target.src = 'img/picA.jpg';
});