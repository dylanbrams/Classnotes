brackets = [
    (3350, 0.05),
    (5050, 0.07),
    (116600, 0.09),
    (None, 0.099)
]

taxable_income = float(input("How much taxable income do you have this year?"))
# Remaining Taxable Income - incrementally reduced.
remaining_inc = taxable_income
# Current iteration through tax brackets
curr_iteration = 0
# Taxes due per tax bracket
taxes_due = []
# Total taxes to pay
total_taxes = 0

while remaining_inc > 0:
    # Puts current tax bracket information into brack_info
    brack_info = brackets[curr_iteration]
    brack_inc = brack_info[0]
    brack_rate = brack_info[1]
    taxable_curr = 0
    if (brack_inc != None and remaining_inc > brack_inc):
        remaining_inc = remaining_inc - brack_inc
        taxable_curr = brack_inc
    else:
        taxable_curr = remaining_inc
        remaining_inc = 0
    current_taxes = taxable_curr * brack_rate
    taxes_due.append([taxable_curr, round(current_taxes, 2), brack_rate])
    total_taxes += current_taxes
    curr_iteration += 1
for tax_info in taxes_due:
    # '${:,.2f}'.format(self.total_value)
    print ("The amount " + '${:,.2f}'.format(tax_info[0]) + " was taxed at " +
           '${:,.2f}'.format(tax_info[2]) +
           " for a total of " + '${:,.2f}'.format(tax_info[1]) + ".")
print ("The total taxes paid was: " + '${:,.2f}'.format(total_taxes, 2))
