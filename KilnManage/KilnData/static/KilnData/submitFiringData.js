/**
 * Created by Dylan Brams on 4/20/2017.
 */
'use strict';
var firingSourceForm = $('#frmFiringData');

/**
 * Returns a promise containing the JSON object for submitting the form.
 */
function submitForm() {
  var actionURL = firingSourceForm.attr('action');
  var submitMethod = firingSourceForm.attr('method');
  // This takes the data from the form and packages it up for sending.
  var formData = firingSourceForm.serialize();
  return Promise.resolve($.ajax({
    dataType: 'json',
    url: actionURL,
    method: submitMethod,
    data: formData
  }));
}