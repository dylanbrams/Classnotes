'''
Pig Latin: put input words into pig latin.
'''
vowels = 'aeiouy'
punctuation = '.,-;:\"\'&!\/? '
input_string = input ('Please enter a word to put into pig latin: ')
output_string = input_string.lower().strip(punctuation)
vowel_place = 0
current_iteration = 0
for current_letter in input_string:
    if current_letter in vowels:
        vowel_place = current_iteration
        break
    else:
        current_iteration += 1

if current_iteration < len(input_string):
    output_string = (output_string[vowel_place:]+ output_string[:vowel_place] + 'ay')
    if input_string[-1] in punctuation:
        output_string += input_string[-1]

    if input_string[0].isupper():
        output_string = output_string.capitalize()

    print (input_string + " in Pig Latin is " + output_string)
else:
    print ("No vowels in word.  Invalid word.")