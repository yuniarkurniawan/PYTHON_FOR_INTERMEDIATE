from itertools import combinations, combinations_with_replacement

# mirip dengan permutasi

list_data = [1, 2, 3, 4]
comb = combinations(list_data, 2)
print(f'{list(comb)}')
# akan mencetak [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]

comb = combinations(list_data, 3)
print(f'{list(comb)}')
# akan mencetak [(1, 2, 3), (1, 2, 4), (1, 3, 4), (2, 3, 4)]


comb_wr = combinations_with_replacement(list_data, 2)
print(f'{list(comb_wr)}')
# akan mencetak [(1, 1), (1, 2), (1, 3), (1, 4), (2, 2), (2, 3), (2, 4), (3, 3), (3, 4), (4, 4)]
# dia akan generate nilai sendiri
