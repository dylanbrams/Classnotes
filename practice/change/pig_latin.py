'''
Pig Latin: put input words into pig latin.
'''
VOWELS = 'aeiouy'
PUNCTUATION = '.,-;:\"\'&!\/? '


def find_consonant(word_in):
    """

    :param word_in:
    :return:

    >>> find_consonant("Green")
    2

    >>> find_consonant("orange")
    0

    >>> find_consonant("streetlight")
    3

    >>> find_consonant("aardvark")
    0

    >>> find_consonant("a")
    0

    """
    vowel_place = 0
    current_iteration = 0
    for current_letter in word_in:
        if current_letter in VOWELS:
            vowel_place = current_iteration
            break
        else:
            current_iteration += 1
    return vowel_place

def to_pig_latin(word, vowel_place):
    """
    Inputs a string to make pig latin, along with where in the word the vowel is.  Returns the word in pig latin.
    :param word:
    :param vowel_place:
    :return:
    """
    word_out = ''
    if vowel_place == 0:
        word_out = word + 'way'
    elif vowel_place != None:
        word_out = (word[vowel_place:] + word[:vowel_place] + 'ay')
    else:
        word_out = None
    return word_out

def match_format(word_to_match, word_to_modify):
    """
    Matches punctuation and capitalization from one word to another.
    :param word_to_match:
    :param word_to_modify:
    :return:
    """
    if word_to_match[-1] in PUNCTUATION:
        word_to_modify += word_to_match[-1]

    if word_to_match[0].isupper():
        word_to_modify = word_to_modify.capitalize()
    return word_to_modify

def main():
    input_string = input ('Please enter a word to put into pig latin: ')
    output_string = input_string.lower().strip(PUNCTUATION)
    vowel_place = find_consonant(input_string)
    if vowel_place > len(output_string):
        print("Invalid word.")
    output_string = to_pig_latin(output_string, vowel_place)
    final_string = match_format(input_string, output_string)

    print (input_string + " in Pig Latin is " + final_string)



if __name__ == '__main__':
    main()
    # import doctest
    # doctest.testmod(extraglobs={'t': ConversionClass()})