/**
 * Created by Dylan Brams on 4/20/2017.
 */
'use strict';
var kilnSourceForm = $('#frmKilnData');

/**
 * Returns a promise containing the JSON object for submitting the form.
 */
function submitForm() {
  var actionURL = kilnSourceForm.attr('action');
  var submitMethod = kilnSourceForm.attr('method');
  // This takes the data from the form and packages it up for sending.
  var formData = kilnSourceForm.serialize();
  return Promise.resolve($.ajax({
    dataType: 'json',
    url: actionURL,
    method: submitMethod,
    data: formData
  }));
}