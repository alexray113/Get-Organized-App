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

// Ask user to enter a location. Geocode the location to get its coordinates
// and drop a marker onto the map.
  // document.querySelector('#display-location').addEventListener('click', () => {
  //   const startingLocation = input1.value

  //   const geocoder = new google.maps.Geocoder();
  //   geocoder.geocode({ address: startingLocation }, (results, status) => {
  //     if (status === 'OK') {
  //       // Get the coordinates of the user's location
  //       const startingLocation = results[0].geometry.location;

  //       // Create a marker
  //       new google.maps.Marker({
  //         position: startingLocation,
  //         map,
  //       });

  //       // Zoom in on the geolocated location
  //       map.setCenter(startingLocation);
  //       map.setZoom(18);
  //     } else {
  //       alert(`Geocode was unsuccessful for the following reason: ${status}`);
  //     }
  //   });
  // });

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
        directionsRenderer.setDirections(response);
      } else {
        alert(`Directions request unsuccessful due to: ${status}`);
      }
    });
    },1000);
  });
}