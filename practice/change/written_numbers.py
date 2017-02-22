keep_running = True
while keep_running:
#def written_numbers(input_num):
    print_num = int(input("Please enter your number between 1 and 99:"))
    print_str = str(print_num) + " "
    if print_num == 10: print_str += "ten"
    if print_num == 11: print_str += "eleven"
    if print_num == 12: print_str += "twelve"
    if print_num == 13: print_str += "thirteen"
    if print_num == 14: print_str += "fourteen"
    if print_num == 15: print_str += "fifteen"
    if print_num == 16: print_str += "sixteen"
    if print_num == 17: print_str += "seventeen"
    if print_num == 18: print_str += "eighteen"
    if print_num == 19: print_str += "nineteen"


    if (print_num > 19 or print_num < 10):
        if (print_num // 10 == 2):
            print_str += "twenty"
        if (print_num // 10 == 3):
            print_str += "thirty"
        if (print_num // 10 == 4):
            print_str += "forty"
        if (print_num // 10 == 5):
            print_str += "fifty"
        if (print_num // 10 == 6):
            print_str += "sixty"
        if (print_num // 10 == 7):
            print_str += "seventy"
        if (print_num // 10 == 8):
            print_str += "eighty"
        if (print_num // 10 == 9):
            print_str += "ninety"

        ones_place = print_num % 10
        if (print_num > 19 and ones_place > 0):
            print_str += "-"

        if (ones_place == 1):
            print_str = print_str + "one"
        elif (ones_place == 2):
            print_str = print_str + "two"
        elif (ones_place == 3):
            print_str = print_str + "three"
        elif (ones_place == 4):
            print_str = print_str + "four"
        elif (ones_place == 5):
            print_str = print_str + "five"
        elif (ones_place == 6):
            print_str = print_str + "six"
        elif (ones_place == 7):
            print_str = print_str + "seven"
        elif (ones_place == 8):
            print_str = print_str + "eight"
        elif (ones_place == 9):
            print_str = print_str + "nine"
    print (print_str)
    keep_running_check = input ("Do you want to keep running? (y)")
    if (keep_running_check != 'y' and keep_running_check != 'Yes'):
        keep_running = False
