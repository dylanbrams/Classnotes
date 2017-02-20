
money_input = round(float(input
                    ("What amount would you like dispensed in change?  ")), 2)
twenties_changed = money_input // 20
change_running_total = money_input - twenties_changed * 20
tens_changed = change_running_total // 10
change_running_total = change_running_total - tens_changed * 10
fives_changed = change_running_total // 5
change_running_total = change_running_total - fives_changed * 5
ones_changed = change_running_total // 1
change_running_total = change_running_total - ones_changed * 1
quarters_changed = change_running_total // .25
change_running_total = change_running_total - quarters_changed * .25
dimes_changed = change_running_total // .10
change_running_total = change_running_total - dimes_changed * .10
nickels_changed = change_running_total // .05
change_running_total = change_running_total - nickels_changed * .05
pennies_changed = (round(change_running_total, 2)) * 100

print ("Twenties Changed: " + str(twenties_changed))
print ("Tens Changed: " + str(tens_changed))
print ("Fives Changed: " + str(fives_changed))
print ("Ones Changed: " + str(ones_changed))
print ("Quarters Changed: " + str(quarters_changed))
print ("Nickels Changed: " + str(dimes_changed))
print ("Dimes Changed: " + str(nickels_changed))
print ("Pennies Changed: " + str(pennies_changed))

