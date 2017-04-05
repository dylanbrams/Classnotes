'use strict';

function appendToTextLI(input) {
  var node = document.createElement('LI');                 // Create a <li> node
  var textnode = document.createTextNode(input);         // Create a text node
  node.appendChild(textnode);                              // Append the text to <li>
  document.getElementById('TextLI').appendChild(node);     // Append <li> to <ul> with id="myList"
}

var namesToAges = {
  'Alyssa': 22,
  'Charley': 25,
  'Dan': 25,
  'Jeff': 20,
  'Kasey': 20,
  'Kim': 20,
  'Morgan': 25,
  'Ryan': 25,
  'Stef': 22
};

function findRarestAge(invar) {
  var values = _.values(invar);
  var valueToCount = _.countBy(values);
  var possiblemin = _.min(_.values(valueToCount));
  var minByResult = _.minBy(valueToCount, function(value) {return valueToCount[value];});
  return minByResult;
}

function findRarestKeys(obj) {
  var valueToKeys = _.groupBy(_.keys(obj), function(key) {
    return obj[key];
  });
  return _.minBy(_.values(valueToKeys), function(keys) {
    return keys.length;
  });
}

function useMinBy(invar2){
  var result = _.minBy(invar2, function(o){return o.val});
}
var result = findRarestAge(namesToAges);
var result2 = useMinBy({'Dylan': 12, 'Sydney': 32, 'Justin': 28});
var result3 = findRarestKeys(namesToAges);
appendToTextLI(result);
appendToTextLI(result2);
appendToTextLI(result3);
