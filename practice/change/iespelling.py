'''
IE Spelling
Inputs a word, looks for the letters 'ie' and 'ei' in sequence in it.  Outputs whether or not the word follows the rule:
 'i before e except after c'
 four cases:
    I before E, after C. -> fail.
    E before I, not after C. -> fail.
    I before E, not after C. -> pass.
    E before I, after C. -> pass.
'''


run_again_flag = True
while (run_again_flag == True):
    in_str = input("Please input a word string: ")
    word_place_cie = in_str.lower().find('cie')
    word_place_ei = in_str.lower().find('ei')
    if ((word_place_ei != -1 and in_str[word_place_ei - 1] != 'c')
        or word_place_cie != -1):
        print(in_str + " does not follow the rule")
    else:
        print(in_str + " follows the rule.")

    run_again = input ('Run Again.')
    if run_again.lower()[:1] != 'y':
        run_again_flag = False
