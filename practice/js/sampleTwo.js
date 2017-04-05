'use strict';

function appendToTextUL(input) {
  var myLi = $('#TextUL');
  var newUL = $('<li>' + input + '</li>');
  $('#TextUL').append(newUL);
}

$('#TextUL').on('click', function() {
  appendToTextUL('Clicked!');  //> "big-button"
});

function AccountPrototype() {
  /**
  * sets up an account object.
  */
  this.title = '';
  this.balance = 0;
  this.deposit = function(input) {
    /*
    * Adds the input to the balance.
    */
    this.balance += input;
  };
  this.withdraw = function(input) {
    /*
    * subtcracts input from balance
    */
    this.balance -= input;
  };
}


function CheckingAccount() {
  /*
  * A checking account that inherits from AccountPrototype to add a withdrawal
  * fee and check book cost.
  */
  this.withdrawalFee = 1.00;
  this.checkBookCost = 15;
}
CheckingAccount.prototype = AccountPrototype;

function SavingsAccount() {
  /*
  * A savings account that inherits from AccountPrototype to add an interest
  * rate and minimum balance
  */
  this.interestRate = .013;
  this.minimumBalance = 100;
}
SavingsAccount.prototype = AccountPrototype;


var myAccount = new AccountPrototype();
myAccount.deposit(100);
myAccount.withdraw(22.54);
appendToTextUL(myAccount.balance);

var DChecking = new CheckingAccount();
appendToTextUL(DChecking.withdrawalFee);
appendToTextUL(DChecking.checkBookCost);

var DSavings = new SavingsAccount();
appendToTextUL(DSavings.interestRate);
appendToTextUL(DSavings.minimumBalance);
//$('#TextUL').addClass('colormytext');
//alert(myAccount.balance);
