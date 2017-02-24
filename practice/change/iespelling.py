'''
IE Spelling
Inputs a word, looks for the letters 'ie' and 'ei' in sequence in it.  Outputs whether or not the word follows the rule:
 'i before e except after c'

'''

def check_ie_adherence(in_str):
    '''

    This function takes as an input a string and outputs the result from four cases and a default:
        I before E, after C. -> fail.
        E before I, not after C. -> fail.
        I before E, not after C. -> pass (general case / default)
        E before I, after C. -> pass.
        default -> pass.
    :param in_str: string to check rule against.
    :return:

    >>> check_ie_adherence('believe')
    believe follows the rule
    >>> check_ie_adherence('ceiling')
    ceiling follows the rule
    >>> check_ie_adherence('science')
    science does not follow the rule
    >>> check_ie_adherence('weird')
    weird does not follow the rule

    '''

    word_place_cie = in_str.lower().find('cie')
    word_place_ei = in_str.lower().find('ei')
    # two options for failure
    if ((word_place_ei != -1 and in_str[word_place_ei - 1] != 'c')
        or word_place_cie != -1):
        print(in_str + " does not follow the rule")
    # Default Success
    else:
        print(in_str + " follows the rule")


def main():
    run_again_flag = True
    while (run_again_flag == True):
        in_str = input("Please input a word string: ")
        check_ie_adherence(in_str)
        run_again = input ('Run Again.')
        if run_again.lower()[:1] != 'y':
            run_again_flag = False

if __name__ == '__main__':
    main()