'use strict';

/*  NOTE: You need to place a ../secrets/forecastapikey.js file containing a
  * declaration of FORECAST_API_KEY with a valid Forecast api key file

/**
 * Get the forecast for a given location.
 *
 * Returns a promise.
 */
function getForecast(lat, lng) {
  var PARAMS = {'units': 'us'};
  var url = 'https://api.forecast.io/forecast/' + FORECAST_API_KEY + '/' + lat + ',' + lng;
  return Promise.resolve($.ajax({
    dataType: 'jsonp',
    url: url,
    data: PARAMS
  }));
}

function mapclickhandler(lat, lng) {
  $('#Latitude').val(lat);
  $('#Longitude').val(lng);
}

function registerMapEventHandlers(map) {
  map.addListener('click', function(event) {
    var lat = event.latLng.lat();
    var lng = event.latLng.lng();
    mapclickhandler(lat, lng);
  });
}

/**
 * Update the forecast paragraph with some text.
 */
function updateForecastParagraph(forecastText) {
  $('#forecast').text(forecastText);
}

/**
 * Create a string description from a forecast.
 */
function formatForecastResult(forecastResult) {
  return 'Temp: ' + forecastResult.currently.temperature + ' F';
}

function formatForecastResult(forecastResult) {
  return 'Temp: ' + forecastResult.currently.temperature + ' F';
}

function getWeatherAtCoords() {
  var lat = $('#Latitude').val();
  var lng = $('#Longitude').val();

  updateForecastParagraph('Loading...');

  getForecast(lat, lng).
    then(function(forecastResult) {
      var forecastText = formatForecastResult(forecastResult);
      updateForecastParagraph(forecastText);
    }).
    catch(function(error) {
      updateForecastParagraph('Error occured. ' + error.statusText);
    });
}


function registerButtonEventHandler() {
  $('#getForecast').click(function() {
    getWeatherAtCoords();
  });
}

/**
 * Return the element to be used as a Google Map.
 */
function getMapElement() {
  return $('#map')[0];
}

/**
 * Create a Google Map on a given element and return the map object.
 */
function createMap(mapElement) {
  //var mycenter = new google.maps.LatLng(-123, 68);
  var mycenter = new google.maps.LatLng(-34.397, 150.644);
  return new google.maps.Map(mapElement, {
    center: mycenter,
    zoom: 8
  });
}


/**
 * Initialize the page on load.
 */
function runInitPage() {
  var mapElement = getMapElement();
  var map = createMap(mapElement);

  registerMapEventHandlers(map);
  $('#Latitude').val(map.center.lat);
  $('#Longitude').val(map.center.lng);
  registerButtonEventHandler();
  // Setup some initial values.
  //runForecast(map.center.lat(), map.center.lng());
}

$(document).ready(runInitPage);
