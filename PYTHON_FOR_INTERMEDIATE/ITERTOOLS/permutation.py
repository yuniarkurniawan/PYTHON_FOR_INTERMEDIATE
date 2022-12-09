from itertools import permutations

# fungsi permutasi akan generate permutasi dari setiap elemen list

def data_permutation(list_data, number):
    perm = permutations(list_data, number)
    print(list(perm))


list_data = [1, 2, 3]
data_permutation(list_data, 3)
# akan mencetak [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]
# list elemen berupa tuple

data_permutation(list_data, 2)
# akan mencetak [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]

data_permutation(list_data, 1)
# akan mencetak [(1,), (2,), (3,)]


perm_2 = permutations(list_data,2)
print(type(perm_2))
# akan mencetak <class 'itertools.permutations'>

hasil = list(perm_2)
print(hasil)
for val in hasil:
    print(val)
# akan mencetak 
# (1, 2)
# (1, 3)
# (2, 1)
# (2, 3)
# (3, 1)
# (3, 2)

print(f'Hasil indek ke 0 : {hasil[0]}')
# akan mencetak Hasil indek ke 0 : (1, 2)

list_data_2 = ['a', 1, 'c']
perm_3 = permutations(list_data_2, 2)
print(list(perm_3))
# akan mencetak [('a', 1), ('a', 'c'), (1, 'a'), (1, 'c'), ('c', 'a'), ('c', 1)]
