"""
Sum Pairs:
    Input a list of integers followed by a single integer
        ([1, 2, 3, 4, 6, -2, -3, -1, 5, 9, 0], 4)
    Check whether the list of integers contains any pairs that sum into the single integer.
    Output those pairs.
"""

import itertools
myNumbers = (1, 2, 3, 4, 6, -2, -3, -1, 5, 9, 0)
myResults = []
# Outer loop: all myNumbers members with an index and the value of that index.
for index, value in enumerate(myNumbers):
    # Inner loop: all myNumbers members after the current index
    for i in myNumbers[(index+1):len(myNumbers)]:
#        print (str(value) + ',' + str(i))
        if (int(value) + int(i) == 1):
                myResults.append((int(value), int(i)))

print (myResults)
#for index, value in enumerate(myNumbers):
#    for i in myNumbers[(index+1):len(myNumbers)]:
#        print (str(value) + ',' + str(i))
