list_bilangan = [1, 2, 3, 4, 5, 6, 7, 8]
pertama, kedua, *range_bilangan, before_last, last = list_bilangan
print(pertama)
print(kedua)
print(range_bilangan)
print(before_last)
print(last)
# akan mencetak
# 1
# 2
# [3, 4, 5, 6]
# 7
# 8

list_nilai = [1, 2, 3, 4]
list_nilai_2 = [4, 5, 6, 7]

list_nilai_3 = [*list_nilai, *list_nilai_2]
print(list_nilai_3)
# akan mencetak [1, 2, 3, 4, 4, 5, 6, 7]

# a_list = []
# a_list.append(*list_nilai)
# print(a_list)
# akan mencetak TypeError: append() takes exactly one argument (4 given)

dict_a = {'a': 1, 'b': 2}
dict_b = {'c': 3, 'd': 4}

new_dict = {**dict_a, **dict_b}
print(new_dict)
# akan mencetak {'a': 1, 'b': 2, 'c': 3, 'd': 4}
