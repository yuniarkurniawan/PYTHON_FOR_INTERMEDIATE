from itertools import product

list_a = [1, 2]
list_b = [3, 4]

data = product(list_a, list_b)
print(f'{list(data)}')
# akan mencetak [(1, 3), (1, 4), (2, 3), (2, 4)]
