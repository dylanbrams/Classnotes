continue_changing = 'y'
twenties_changed_total = 0
tens_changed_total = 0
fives_changed_total = 0
ones_changed_total = 0
quarters_changed_total = 0
dimes_changed_total = 0
nickels_changed_total = 0
pennies_changed_total = 0

while (continue_changing == 'y'):
    money_input = round(float(input
                        ("What amount would you like dispensed in change?  ")), 2)
    twenties_changed = money_input // 20
    twenties_changed_total += twenties_changed
    change_running_total = money_input - twenties_changed * 20
    tens_changed = change_running_total // 10
    tens_changed_total += tens_changed
    change_running_total -= tens_changed * 10
    fives_changed = change_running_total // 5
    fives_changed_total += fives_changed
    change_running_total -= fives_changed * 5
    ones_changed = change_running_total // 1
    ones_changed_total += ones_changed
    change_running_total -= ones_changed * 1
    quarters_changed = change_running_total // .25
    quarters_changed_total += quarters_changed
    change_running_total -= quarters_changed * .25
    dimes_changed = change_running_total // .10
    dimes_changed_total += dimes_changed
    change_running_total -= dimes_changed * .10
    nickels_changed = change_running_total // .05
    change_running_total -= nickels_changed * .05
    nickels_changed_total += nickels_changed
    pennies_changed = (round(change_running_total, 2)) * 100
    pennies_changed_total += pennies_changed


    if (twenties_changed > 0):
        print ("Twenties Changed: " + str(int(twenties_changed)))
    print ("Tens Changed: " + str(int(tens_changed)))
    print ("Fives Changed: " + str(int(fives_changed)))
    print ("Ones Changed: " + str(int(ones_changed)))
    print ("Quarters Changed: " + str(int(quarters_changed)))
    print ("Nickels Changed: " + str(int(dimes_changed)))
    print ("Dimes Changed: " + str(int(nickels_changed)))
    print ("Pennies Changed: " + str(int(pennies_changed)))
    continue_changing = input ('Enter \'y\' to dispense more change.')

print ("Total Twenties Changed: " + str(int(twenties_changed_total)))
print ("Total Tens Changed: " + str(int(tens_changed_total)))
print ("Total Fives Changed: " + str(int(fives_changed_total)))
print ("Total Ones Changed: " + str(int(ones_changed_total)))
print ("Total Quarters Changed: " + str(int(quarters_changed_total)))
print ("Total Nickels Changed: " + str(int(dimes_changed_total)))
print ("Total Dimes Changed: " + str(int(nickels_changed_total)))
print ("Total Pennies Changed: " + str(int(pennies_changed_total)))

