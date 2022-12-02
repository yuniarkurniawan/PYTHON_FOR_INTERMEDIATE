from collections import namedtuple

# deklarasi namedtupe(<nama_object>,[<nama_field>])
Person = namedtuple('Person', ['nama', 'sex', 'alamat'])

person = Person(nama='Yuniar', sex='Pria', alamat='Bandung')
print(f'Nama : {person.nama}')
print(f'Sex : {person.sex}')
print(f'Alamat : {person.alamat}')
# akan mencetak 
# Nama : Yuniar
# Sex : Pria
# Alamat : Bandung
