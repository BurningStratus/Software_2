/*
Routing with digitransit (16p)

Not for the faint-hearted. Don't do this if it interferes with the project. It's not worth it.
Create an app that shows the route from user defined address to school (Karaportti 2).

You need to have a form where user adds an address. 
After the form is submitted, the route is displayed on a map. 
Show also the starting and ending time of the trip. 
Not each part, just the start and end times.

Example: JS, HTML
    You'll need this Leaflet plugin to make the example work.
Here is an example on how to use places/addresses with coordinates.
    To get coordinates from address, you can use address search
    
    
    If you get cors errors (which is likely not going to happen) use this fix.
*/

'use strict';

// sources:
// https://digitransit.fi/en/developers/apis/1-routing-api/itinerary-planning/
// route points are in Google polyline encoded format, so you need to add support for Leafletiin:
// https://github.com/jieter/Leaflet.encoded


// show the map
const map = L.map('map').setView([60.1785553, 24.8786212], 13);
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
}).addTo(map);

const apiAddress = 'https://api.digitransit.fi/routing/v1/routers/hsl/index/graphql'; // cors issues may arise, use proxy or browser plugin if necessary

// fetch route with origin and target
function getRoute(origin, target) {
    // GraphQL query
    const GQLQuery = `{
  plan(
    from: {lat: ${origin.latitude}, lon: ${origin.longitude}}
    to: {lat: ${target.latitude}, lon: ${target.longitude}}
    numItineraries: 1
  ) {
    itineraries {
      legs {
        startTime
        endTime
        mode
        duration
        distance
        legGeometry {
          points
        }
      }
    }
  }
}`;

    const fetchOptions = {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
      'digitransit-subscription-key': 'your key here',
        },
        body: JSON.stringify({query: GQLQuery}),
    };

    fetch(apiAddress, fetchOptions).then(function (response) {
        return response.json();
    }).then(function (result) {
        console.log(result.data.plan.itineraries[0].legs);
        const googleEncodedRoute = result.data.plan.itineraries[0].legs;
        for (let i = 0; i < googleEncodedRoute.length; i++) {
            let color = '';
            switch (googleEncodedRoute[i].mode) {
                case 'WALK':
                    color = 'green';
                    break;
                case 'BUS':
                    color = 'red';
                    break;
                case 'RAIL':
                    color = 'cyan'
                    break;
                case 'TRAM':
                    color = 'magenta'
                    break;
                default:
                    color = 'blue';
                    break;
            }
            const route = (googleEncodedRoute[i].legGeometry.points);
            const pointObjects = L.Polyline.fromEncoded(route).getLatLngs(); // fromEncoded: convert Google encoding to Leaflet polylines
            L.polyline(pointObjects).setStyle({
                color
            }).addTo(map);
        }
        map.fitBounds([[origin.latitude, origin.longitude], [target.latitude, target.longitude]]);
    }).catch(function (e) {
        console.error(e.message);
    });
}

// get route from origin to target
getRoute({latitude: 60.24, longitude: 24.74}, {latitude: 60.16, longitude: 24.92})