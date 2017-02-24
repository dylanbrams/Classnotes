"""An object-oriented solution to the cash register problem."""

class ChangeMachine(object):
    """A single change machine object.  Change machines have the following properties:
        local_change_set: a change_set object containing all the change inside the register
    """
    def __init__(self, local_change_set):
        self.local_change_set = local_change_set

class Change_Set(object):
    """
        A change set object.  Contains a collection of all the types of change available and their counts.

        fifties, twenties, tens, fives, ones, quarters, dimes, nickels, and pennies.  All integers.
    """
    def __init__(self, fifties, twenties, tens, fives, ones, quarters, dimes, nickels, pennies , total_value):
        '''
        Initializes a change set.  Pass in a zero for total value to have it calculated for you.
        :param fifties:
        :param twenties:
        :param tens:
        :param fives:
        :param ones:
        :param quarters:
        :param dimes:
        :param nickels:
        :param pennies:
        :param total_value:
        '''
        self.fifties = fifties
        self.twenties = twenties
        self.tens = tens
        self.fives = fives
        self.ones = ones
        self.quarters = quarters
        self.dimes = dimes
        self.nickels = nickels
        self.pennies = pennies
        if (total_value == None  or total_value > 0):
            self.total_value = total_value
        else:
            self.total_value = (50 * fifties + 20 * twenties + 10 * tens + 5 * fives + 1 * ones +
                                .25 * quarters + .10 * dimes + .05 * nickels + .01 * pennies)

    def __init__(self):
        '''
        Initializes an empty change set.
        '''
        self.fifties = 0
        self.twenties = 0
        self.tens = 0
        self.fives = 0
        self.ones = 0
        self.quarters = 0
        self.dimes = 0
        self.nickels = 0
        self.pennies = 0
        self.total_value = 0

    def change_amount(self, amount):
        '''
        Converts an input amount to a change set.
        :param amount:
        :return:
        '''
        self.total_value = amount
        running_total = amount
        self.fifties = self.denomination_change(50, running_total)
        running_total -= self.fifties * 50
        self.twenties = self.denomination_change(20, running_total)
        running_total -= self.twenties * 20
        self.tens = self.denomination_change(10, running_total)
        running_total -= self.tens * 10
        self.fives = self.denomination_change(5, running_total)
        running_total -= self.fives * 5
        self.ones = self.denomination_change(1, running_total)
        running_total -= self.ones
        self.quarters = self.denomination_change(.25, running_total)
        running_total -= self.quarters * .25
        self.dimes = self.denomination_change(.10, running_total)
        running_total -= self.dimes * .10
        self.nickels = self.denomination_change(.05, running_total)
        running_total -= self.nickels * .05
        self.pennies = self.denomination_change(.01, running_total)
        running_total -= self.pennies * .01
        if round(running_total, 2) > 0:
            print("Error: accurate change was not provided.")


    def denomination_change(self, denomination_amount, value):
        """Returns the count of a particular denomination included in a value."""
        if value > .01:
            return int(value // denomination_amount)
        elif value == .01:
            # Math around pennies is different because of the errors involved in Python's float calculations.
            return int(round((value * 100),0))
        else:
            return 0
        print("Denomination Amount: " + str(denomination_amount) + " denomination_count: " + str(denomination_count) +
              " value: "+ str(value) + "ID : " + str(id(denomination_count)))

    def print_change(self):
        '''
        Print out the total amount of change in the current set and what that set contains.
        :return:
        '''
        print("Current Change Value: " + '${:,.2f}'.format(self.total_value) )
        if self.fifties > 0:
            print (str(self.fifties) + " : fifties")
        if self.twenties > 0:
            print (str(self.twenties) + " : twenties")
        if self.tens > 0:
            print (str(self.tens) + " : tens")
        if self.fives > 0:
            print (str(self.fives) + " : fives")
        if self.ones > 0:
            print (str(self.ones) + " : ones")
        if self.quarters > 0:
            print (str(self.quarters) + " : quarters")
        if self.dimes > 0:
            print (str(self.dimes) + " : dimes")
        if self.nickels > 0:
            print (str(self.nickels) + " : nickels")
        if self.pennies > 0:
            print (str(self.pennies) + " : pennies")


def main():

    more_change = True
    while (more_change == True):
        #register.make_change(change_running_total)
        money_input = round(float(input
                                  ("What amount would you like dispensed in change?  ")), 2)
        current_change = Change_Set()
        current_change.change_amount(money_input)
        current_change.print_change()

        get_change = input ('Dispense more change.')
        if get_change.lower()[:1] != 'y':
            more_change = False

if __name__ == '__main__':
    main()