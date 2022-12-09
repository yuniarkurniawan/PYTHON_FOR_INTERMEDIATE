from itertools import groupby

list_data = [1, 2, 3, 4]
group_data = groupby(list_data, key = lambda x: x<= 3)
for key, val in group_data:
    print(key, list(val)) 
# akan mencetak
# True [1, 2, 2, 3]
# False [4]


persons = [{'name': 'Tim', 'age': 25}, {'name': 'Amstrong', 'age': 25},
           {'name': 'Luis', 'age': 27},{'name': 'Figo', 'age': 28}]

group_data_person = groupby(persons, lambda x: x['age'])
for key, val in group_data_person:
    print(key, list(val))
# akan mencetak
# 25 [{'name': 'Tim', 'age': 25}, {'name': 'Amstrong', 'age': 25}]
# 27 [{'name': 'Luis', 'age': 27}]
# 28 [{'name': 'Figo', 'age': 28}]