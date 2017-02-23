"""
Phone Numbers.Py
Pretty prints Phone numbers in two formats
503-555-1212
and
(503) 555-1212
OR
555-1212
"""

input_number = input("Please enter a phone number.")
if len(input_number) == 10:
    phone_parts = [input_number[:3], input_number[3:6], input_number[6:]]
dashed_phone = '-'.join(phone_parts)
print(dashed_phone)
paren_phone = '({}) {}-{}'.format(phone_parts[0], phone_parts[1], phone_parts[2])
print (paren_phone)

# input_number = input("Please enter a phone number.")
# if len(input_number) == 10:
#     # before the 4th character
#     # between the 4th and the 7th character [included the 4th]
#     # from the 7th on [included the 7th]
#     #print(input_number[:3] + '-' + input_number[3:6] + '-' + input_number[6:])
#     #print('(' + input_number[:3] + ') ' + input_number[3:6] + '-' + input_number[6:])
#
# elif len(input_number) == 7:
#     print(input_number[:3] + '-' + input_number[3:])
# else:
#     print('Invalid number length.  We\'re too lazy for international numbers.')
#
