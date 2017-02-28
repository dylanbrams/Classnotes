
for i in range(1,101):
    strprint = ''
    if (i % 3 == 0):
        strprint += 'fizz'
    if (i % 5 == 0):
        strprint += 'buzz'
    if (strprint == ''):
        strprint += str(i)
    print (strprint)
