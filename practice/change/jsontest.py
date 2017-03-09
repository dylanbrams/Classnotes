# import json
#
# NAME_FIELD_ID = 0
# PHONE_FIELD_ID = 1
#
# from collections import namedtuple
# namedtuple('PersonEntry', ['name', 'phone'] )
# jsonString = '{"name": "David", "phone": "503-123-4567"}'
# PersonEntry = namedtuple('PersonEntry', ['name', 'phone'])
# jsonLoaded = json.loads(jsonString)
# # PersonEntry( [List 1 *names*] , [List 2 *phone numbers*]
# x = PersonEntry(['Dylan', jsonLoaded['name']], ['503-123-5454', jsonLoaded['phone']])
# for current_name in x.name:
#     print(current_name)
#
# PseudoNamedTuple = (['Dylan', jsonLoaded['name']], ['503-123-5454', jsonLoaded['phone']])
# for current_name in x[NAME_FIELD_ID]:
#     print(current_name)
#
#
# print(max(x.name))
# print(max(x.phone))
#


#print(max('1', '2', '3', '123'))
#
dict_one = {'(1, 4)': '3', '(2, 4)': '4', '(1, 4)': '7'}

print (dict_one)
#json_one = json.dumps(dict_one)
#open("savethisobject.txt")

#dict_repopulated = json.loads(json_one)
dict_two = {(1, 4): 5, (2, 4) : 5}
print (dict_two)
dict_two.update({(3, 6): 4})
print (dict_two)
#lookup_key = dict_one[(1, 4)]
looked_up_two = dict_two[(1, 4)]
#print (lookup_key)
print (looked_up_two)
