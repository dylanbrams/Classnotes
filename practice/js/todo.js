'use strict';

function makeComplete(ele) {
  var myparent = $(ele).parent();
  $(myparent).addClass('strikethrough-class');
}

function addListItem(inputtext) {
  var newUL = $('<li> <p>' + inputtext +
  '</p><button class=checkoff>Complete</button>' +
  '</li>');
  $('#ToDoList').append(newUL);
  $('.checkoff').on('click', function() {
    makeComplete(this);
  });
}

$('#AddToDo').on('click', function() {
  var TextBoxString = $('#ToDoText').val();
  addListItem(TextBoxString);  //> "big-button"
});
