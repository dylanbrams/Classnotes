import math
import unit_convert
# Regex processing functions.
import re
import itertools

# numbers2 = [21, 22, 23, 24, 25]
# numbers_a = list(enumerate(numbers2))
# print (numbers2)
# numbers3 = ['Mango' + str(d) if i<=2 else str(d) for i, d in enumerate(numbers2)]
# print (numbers3)
# #numbers4 = for i in numbers2[::2]
# numbers4 = [ int(d)*2 if i%2==0 else d for i, d in enumerate(numbers2)]
#
# print (numbers4)
#
# numbers5 = []
# for i in range(0, len(numbers2)):
#     if i % 2 == 0:
#         numbers5.append(numbers2[i] * 2)
#     else:
#         numbers5.append(numbers2[i])
# print (numbers5)

# big_word_list = "ThisIsAHugeCamelCaseWordThatNeedsToBeSplit"
# word_list_parts = [word.lower() for word in
#                    re.split(r'([A-Z][a-z]*)', big_word_list) if len(word) > 0]
#
# word_list_parts_2 = [word.lower() for word in
#                          re.findall("[A-Z]?[a-z]+|[A-Z]+(?=[A-Z]|$)", big_word_list)]
# print(word_list_parts)
# print(word_list_parts_2)
# wlp_chained = itertools.chain(word_list_parts)
# for i in wlp_chained:
#     print (i)
# print (wlp_chained)


#list_var = [result1 if condition1 else result2 for index, value in enumerate(original_list)]

# blue_array
# WhiteCloud
# string-object
# THIS_IS_A_CONSTANT

# re.split(r'([A-Z][a-z]*)', var_name)

# IDictionaryFile
# iDictionaryFile

import sys

for arg in sys.argv:
    print (arg)



#foo = [['abc', 'defg', 'hijk'], ['lmno', 'pqrs', 'tuvw'], ['xyz', '1234', '56789']]
foo = [['1a', '1b', '1c', '1d'], ['2a', '2b', '2c'], ['xyz', '1234', '56789']]
my_list = [max(len(str(x)) for x in line) for line in zip(*foo)]
#my_list = [max(len(str(x)) for x in line) for line in zip(*foo)]


#print (my_list)
print (foo)
print (list(zip(*foo)))

radians_angle = (45 * 2 * math.pi) / 360
x_movement = math.cos(radians_angle)
y_movement = math.sin(radians_angle)
print(x_movement)
print(y_movement)
x = unit_convert.ConversionClass()

