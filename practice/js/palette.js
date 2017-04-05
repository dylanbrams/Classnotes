'use strict';

function clearErrorDisplay() {
  $('#errors').text('No Current Errors.');
}

function numberErrorCheck(numIn) {
  if (Number(numIn) !== 'NaN') {
    if (0 <= numIn && numIn <= 255) {
      return false;
    }
  }
  $('#errors').text('Invalid Number Entered (0-255, integers only)');
  return true;
}

function getTextBoxColorNumber(boxname) {
  var myNumber = $(boxname).val();
  if (numberErrorCheck(myNumber) === false) {
    return myNumber;
  }  else {
    return 0;
  }
}

function getTextboxes() {
  var RedNum = getTextBoxColorNumber('#RedInput');
  var GreenNum = getTextBoxColorNumber('#GreenInput');
  var BlueNum = getTextBoxColorNumber('#BlueInput');
  var myArray = [RedNum, GreenNum, BlueNum];
  return myArray;
}

$('.ColorInput').change(function() {
  // Clear Error Display
  clearErrorDisplay();
  // Get Text boxes
  var colorNumbers = getTextboxes();
  // Convert to Hex and put into swatch.
  var rgbString = 'rgb(' + colorNumbers[0] + ',' + colorNumbers[1] + ',' + colorNumbers[2] + ')';
  $('.colorswatch-class').css('background-color', rgbString);
});
