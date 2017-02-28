"""
Credit Card Validator - Validates a credit card number according to some weird algorithm that is not standard.
"""

def mult_even_by_two(list_input):
    '''
    Multiplies all the even inputs of the list by two.
    :param list_input:
    :return:

    >>> mult_even_by_two([2, 1, 4])
    [4, 1, 8]
    >>> mult_even_by_two([8, 6, 3, 7, 5, 4, 2])
    [16, 6, 6, 7, 10, 8, 4]
    >>> mult_even_by_two([3])
    [6]

    '''
    list_working = list_input.copy()
    for i in range(0, len(list_input)):
        if (i) % 2 == 0:
            list_working[i] = list_working[i] * 2
    return list_working

def subtract_nine_when_over_ten(list_input):
    """
    Subtracts nine from the value of any members of the input list larger than nine.
    :param list_input:
    :return:

    >>> subtract_nine_when_over_ten([10, 11, 3, 4, 6, 8, 3])
    [1, 2, 3, 4, 6, 8, 3]
    """
    list_working = list_input.copy()
    for i in range(0, len(list_working)):
        list_working[i] = list_working[i] - 9 if list_working[i] > 9 else list_working[i]
    return list_working

def check_card_num(card_number_parts):
    """
    Check whether a list containing card number parts fits this checksum algorithm.
    :param card_number_parts:
    :return:
    """
    card_parts_working = card_number_parts
    last_num = card_number_parts.pop()
    card_parts_working.reverse()
    # Multiply the even (zero-initiated-indexed)
    card_parts_working = mult_even_by_two(card_parts_working)
    card_parts_working = subtract_nine_when_over_ten(card_parts_working)
    # Sum Digits, compare to checksum.
    sum_digits = sum(card_parts_working)
    checksum = sum_digits % 10
    if checksum == last_num:
        return True
    else:
        return False



def main():
    run_again_flag = True
    while (run_again_flag == True):
        in_str = list(input("Please input a credit card number: "))
        in_str_numbers = [int(x) for x in in_str]
        result = check_card_num(in_str_numbers)
        if result == True:
            print ("Passed checksum.")
        else:
            print("Failed Checksum")
        run_again = input('Run Again.')
        if run_again.lower()[:1] != 'y':
            run_again_flag = False
if __name__ == '__main__':
    main()