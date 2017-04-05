'use strict';

function appendToTextLI(input) {
  var node = document.createElement('LI');                 // Create a <li> node
  var textnode = document.createTextNode(input);         // Create a text node
  node.appendChild(textnode);                              // Append the text to <li>
  document.getElementById('TextLI').appendChild(node);     // Append <li> to <ul> with id="myList"
}

/**
* Makes a string into leetspeek
*/
function makeLeet(inputSentence) {
  // Converts a string to leetspeek, puts that string in UL TextLI on the page.
  // Dictionary of values to replace.
  var dictionary = {
    'o': '0',
    'l': '1',
    'e': '3',
    'a': '4',
    't': '7'
  };
  var wordsToProcess = inputSentence.split(' '); // Words to split into values.
  // Loops through each word.
  for (var i = 0; i < wordsToProcess.length; i += 1) {
    var value = wordsToProcess[i];
    // Replaces individual characters
    for (var replaceKey in dictionary) {
      value = value.replace(replaceKey, dictionary[replaceKey]);
    }
    // Appends the final value to an LI element.
    appendToTextLI(value);
  }
}

makeLeet('this is a test sentence.  fathers brought forth on this continent');
function useCountBy(invar) {
  var result = _.countBy(invar, function(c) {return c.includes('t');})
  return result;
}

function useMinBy(invar2){
  var result = _.minBy(invar2, function(o){return o.val});
}
var result = useCountBy(['this', 'sentence', 'is', 'a', 'collection']);
var result2 = useMinBy({'Dylan': 12, 'Sydney': 32, 'Justin': 28});
appendToTextLI(result['true']);
appendToTextLI(result2);

//makeLI();
