'use strict';

function getNearbyStops(latLng) {
  return Promise.resolve($.ajax({
    dataType: 'jsonp',
    url: 'https://developer.trimet.org/ws/V1/stops',
    data: {
      appID: TRIMET_APP_ID,
      json: true,
      ll: latLng.join(','),
      meters: 100,
      showRoutes: true
    }
  }));
}
var getPosition = function(options) {
  return new Promise(function(resolve, reject) {
    navigator.geolocation.getCurrentPosition(resolve, reject, options);
  });
};

function positionToStops(position) {
  var latitude  = position.coords.latitude;
  var longitude = position.coords.longitude;

  var myLatLng = [latitude, longitude];
  return getNearbyStops(myLatLng);
}


function processStops(trimetresult) {
  console.log(trimetresult);
  var stops = trimetresult.resultSet.location;
  console.log(stops);
}

var output = document.getElementById('out');

getPosition().
  then(positionToStops).
  then(processStops).
  catch(function(err) {
    console.log(err);
  });
