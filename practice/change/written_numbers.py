"""
Written Numbers:
    Outputs a written string representing an inputted integer.
"""

words_lookup = {1: "one", 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine',
                10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen',
                16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen',
                20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty',
                60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety'}

def print_single(print_num, words_lookup):
    """
    returns a printable string representing a single-word number.  E.G. : 9

    >>> print_single(4, words_lookup)
    'four'
    >>> print_single(14, words_lookup)
    'fourteen'

    :param print_num:
    :param words_lookup:
    :return:
    """
    print_string = words_lookup[int(print_num)]

    return print_string

def print_two_part(print_num, words_lookup):
    addition_str = ''
    ones_place = int(print_num) % 10
    tens_place = int(print_num // 10) * 10
    tens_word = words_lookup[tens_place]
    ones_word = words_lookup[ones_place]
    addition_str += tens_word + "-" + ones_word
    return addition_str

def print_number(print_num):
    print_word = str(print_num) + ' '
    if (print_num < 21):
        print_word += print_single(print_num, words_lookup)
    else:
        print_word += print_two_part(print_num, words_lookup)
    print(print_word)

def main():
    run_again_flag = True
    while (run_again_flag == True):
        in_str = input("Please input a numeric string between 1 and 99: ")
        print_number(int(in_str))
        run_again = input('Run Again.')
        if run_again.lower()[:1] != 'y':
            run_again_flag = False


if __name__ == '__main__':
    main()