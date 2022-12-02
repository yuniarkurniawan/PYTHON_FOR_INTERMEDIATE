from collections import Counter

# fungsi Counter(<data_string_atau_list>) akan return dictionary yang
# berisi key = elemen, dan value = jumlah dari elemen tersebut
list_data = list('aabbccaagbggvvaa')
tmp_counter = Counter(list_data)
print(tmp_counter)
# akan mencetak Counter({'a': 6, 'b': 3, 'g': 3, 'c': 2, 'v': 2})

# fungsi .most_common(<n>) digunakan untuk menampilkan sebanyak n data terbanyak
print(tmp_counter.most_common(2))
# akan mencetak Counter({'a': 6, 'b': 3})
print(tmp_counter.most_common(3))
# akan mencetak Counter({'a': 6, 'b': 3, 'g': 3})


# seperti pada dictionary untuk iterasi dapat menggunakan items(), keys()
# dan values()
for key, val in tmp_counter.items():
    print(f'Key {key} : Value {val}')
# akan mencetak 
# Key a : Value 6
# Key b : Value 3
# Key c : Value 2
# Key g : Value 3
# Key v : Value 2


for key in tmp_counter.keys():
    print(f'Key : {key}')
# akan mencetak
# Key : a
# Key : b
# Key : c
# Key : g
# Key : v


for val in tmp_counter.values():
    print(f'Value : {val}')
# akan mencetak
# Value : 6
# Value : 3
# Value : 2
# Value : 3
# Value : 2


# fungsi update untuk merubah/menambah struktur dictionary bisa dilakukan
tmp_counter.update({'a': 5, 'c': 6, 'b':3})
for key, val in tmp_counter.items():
    print(f'Key {key} : Value : {val}')
#akan mencetak dictionary baru 
# Key a : Value : 11 // jumlah elemen a bertambah 5 menjadi 11
# Key b : Value : 6 // jumlah elemen b  bertambah 3 menjadi 6
# Key c : Value : 8 // jumlah elemen c bertambah 6 menjadi 8
# Key g : Value : 3
# Key v : Value : 2


# fungsi del <nama_dict>[<key>] dan <nama_dict>.pop(<key>) dapat digunakan
# untuk menghapus data
tmp_counter.pop('a')
print(f'Setelah pop(\'a\') : {tmp_counter}')
# akan mencetak Setelah pop('a') : Counter({'c': 8, 'b': 6, 'g': 3, 'v': 2})

del tmp_counter['b']
print(f'Setelah del tmp_counter[\'b\'] {tmp_counter}')
# akan mencetak Setelah del tmp_counter['b'] Counter({'c': 8, 'g': 3, 'v': 2})


tmp_counter.subtract({'c': 2, 'g': 1})
print(f'Setelah substract() {tmp_counter}')
# akan mencetak Counter({'c': 6, 'g': 2, 'v': 2})
# key c dikurangi 2 menjadi 6
# key g dikurangi 1 menjadi 1


# fungsi elements() digunakan untuk generate kembali
tmp_list = list(tmp_counter.elements())
print(f'Setelah elements() {tmp_list}')
# akan mencetak Setelah elements() ['c', 'c', 'c', 'c', 'c', 'c', 'g', 'g', 'v', 'v']