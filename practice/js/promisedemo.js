'use strict';
var getPosition = function(options) {
  return new Promise(function(resolve, reject) {
    navigator.geolocation.getCurrentPosition(resolve, reject, options);
  });
};

function latLongAlert(myLatLong) {
  alert(myLatLong);
}

var output = document.getElementById('out');

var myLatLong = getPosition().then(function(position) {
  var latitude  = position.coords.latitude;
  var longitude = position.coords.longitude;

  output.innerHTML = '<p>Latitude is ' + latitude + '° <br>Longitude is ' +
    longitude + '°</p>';

  var img = new Image();
  img.src = 'https://maps.googleapis.com/maps/api/staticmap?center=' +
    latitude + ',' + longitude + '&zoom=13&size=300x300&sensor=false';

  output.appendChild(img);
  console.log(output);
  latLongAlert(latitude, longitude);
  return [latitude, longitude];
}).catch(function(err) {
  output.innerHTML = 'Unable to retrieve your location';
  console.log(err);
});

alert(myLatLong);
