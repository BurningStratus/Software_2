
// map stash

// https://c.tile.thunderforest.com/spinal-map/4/8/3.png?apikey=6a53e8b25d114a5e9216df5bf9b5e9c8
// https://c.tile.thunderforest.com/spinal-map/{z}/{x}/{y}.png
// stamen-tiles-{S}a.ssl.fastly.net/terrain/{Z}/{X}/{Y}.png
// tiles.stadiamaps.com/tiles/stamen_{Z}/{X}/{Y}
// 'https://tile.openstreetmap.org/{z}/{x}/{y}.png'


let lat, long, unidetifiedInteger;
lat = parseFloat(prompt('latitude of your choice:'));
long = parseFloat(prompt('longitude of your choice:'));
unidetifiedInteger = parseFloat(prompt('random number of your choice:'));

let map = L.map('map').setView([lat, long], 13);
L.tileLayer('https://c.tile.thunderforest.com/pioneer/{z}/{x}/{y}.png?apikey=6a53e8b25d114a5e9216df5bf9b5e9c8', {
    maxZoom: 19,
    attribution: '&copy; Deus Ex Machina'
}).addTo(map);

let marker = L.marker([lat, long]).addTo(map);



