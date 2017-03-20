import random
list1 = [1, 2, 3]
list2 = [[1, 2, 3], 4, 5, 6]
list3 = [1, 2, 7]
i = list1 in list2
j = list3 in list2
print (i)
print (j)
def test_cards():
    mycards = ['AC', 'AD', 'AS', 'QD']
    cards_old = mycards.copy()
    random.shuffle(mycards)
    if (mycards == cards_old):
        return False
    else:
        return True

x = card()
