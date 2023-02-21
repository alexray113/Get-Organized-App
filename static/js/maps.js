//javascript.js
// set map options
function initMap() {
  map = new google.maps.Map(document.getElementById("map"), {
    center: { lat: 36.162663, lng: -86.781601 },
    zoom: 6,
  });
  infoWindow = new google.maps.InfoWindow();

//create autocomplete objects for all inputs
const options = {
  types: ['geocode', 'establishment']
}

const input1 = document.getElementById("input1");
let autocomplete1 = new google.maps.places.Autocomplete(input1, options);

const input2 = document.getElementById("input2");
let autocomplete2 = new google.maps.places.Autocomplete(input2, options);

    // Display walking directions from origin location to destination
  // on the map
  document.querySelector('#display-directions').addEventListener('click', () => {
    const directionsService = new google.maps.DirectionsService();
    let startingLocation = input1.value
    let finalDestination = input2.value
    let startingCoords = null
    let finalCoords = null
    
    const geocoder1 = new google.maps.Geocoder();
    geocoder1.geocode({ address: startingLocation }, (results, status) => {
      if (status === 'OK') {
        // Get the coordinates of the user's starting location
        let startingLocation = results[0].geometry.location;
        startingCoords = startingLocation
        // Create a marker
        new google.maps.Marker({
          position: startingLocation,
          map,
        });
        
      }
      });
    const geocoder2 = new google.maps.Geocoder();
    geocoder2.geocode({ address: finalDestination }, (results, status) => {
      if (status === 'OK') {
        // Get the coordinates of the user's ending location
        let finalDestination = results[0].geometry.location;
        finalCoords = finalDestination
        // Create a marker
        new google.maps.Marker({
          position: finalDestination,
          map,
          
        });
      }

      });

      

    // The DirectionsRenderer object is in charge of drawing directions
    // on maps
    setTimeout(()=>{
    const directionsRenderer = new google.maps.DirectionsRenderer();
    directionsRenderer.setMap(map);
    const determinedRoute = {
      origin: {
        lat: startingCoords.lat(),
        lng: startingCoords.lng()
      },
      destination: {
        lat: finalCoords.lat(),
        lng: finalCoords.lng()
      },
      travelMode: 'DRIVING',
    };

    directionsService.route(determinedRoute, (response, status) => {
      if (status === 'OK') {
        console.log(response)
        // pulling time and distance from json response and adding to output div
        const output = document.querySelector('#output');
        output.innerHTML = "<div>From: " + document.getElementById("input1").value + ".<br />To: " + document.getElementById("input2").value + ".<br /> Driving distance: " + response.routes[0].legs[0].distance.text + ".<br />Duration: " + response.routes[0].legs[0].duration.text + ".</div>";
        directionsRenderer.setDirections(response);
      } else {
        alert(`Directions request unsuccessful due to: ${status}`);
      }
    });
    },1000);
  });

}