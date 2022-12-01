
# cara deklarasi 1
dict_data_siswa = dict(nrp="2002001",
                       nama="siswa_1",
                       usia=20)

# cara deklarasi 2
dict_data_siswa = {
    "nrp": "2002001",
    "nama": "siswa_1",
    "usia": 20
}


# fungsi items() digunakan untuk iteraing dictionary beserta key
def dict_iterate_data(dict_data):
    
    for key, val in dict_data.items():
        print(f'{key} : {val}')

dict_iterate_data(dict_data_siswa)
# akan mencetak
# nrp : 2002001
# nama : siswa_1
# usia : 20


def dict_iterate_keys_value(dict_data):

    for keys in dict_data.keys():
        print(f'Keys : {keys}')

    for vals in dict_data.values():
        print(f'Values : {vals}')



dict_iterate_keys_value(dict_data_siswa)
# akan mencetak
# Keys : nrp
# Keys : nama
# Keys : usia
# Values : 2002001
# Values : siswa_1
# Values : 20

# untuk menambahkan data baru dapat dilakukan dengan cara
# data_dict[<key_baru>] = <nilai_baru>
def dict_tambah_data_baru(dict_data, **data_baru):
    
    for key, val in data_baru.items():
        if key not in dict_data:
            dict_data[key] = val

    return dict_data

print(dict_tambah_data_baru(dict_data_siswa, sex='Pria'))
# akan mencetak {'nama': 'siswa_1', 'usia': 20, 'nrp': '2002001', 'sex': 'Pria'}


# untuk merubah data lama dapat dilakukan dengan cara
# data_dict[<key_eksis>] = <nilai_baru>
def dict_ubah_data_baru(dict_data, **data_ubah):

    for key, val in data_ubah.items():
        if key in dict_data:
            dict_data[key] = val

    return dict_data

print(dict_ubah_data_baru(dict_data_siswa, usia=60))
# akan mencetak {'nama': 'siswa_1', 'usia': 60, 'nrp': '2002001', 'sex': 'Pria'}


# fungsi del dict_data[<key_ubah>] dan dict_data.pop(<key_data>)
def dict_hapus_data(key_ubah, dict_data):

    # bisa dilakukan dengan kedua cara ini
    
    if key_ubah in dict_data:
        dict_data.pop(key_ubah)

    if key_ubah in dict_data:
        del dict_data[key_ubah]
        
    return dict_data

print(dict_hapus_data('nama', dict_data_siswa))
# akan mencetak {'usia': 60, 'nrp': '2002001', 'sex': 'Pria'}

# fungsi popitem() akan menhapus pada data terakhir dict
def dict_hapus_data_terakhir(dict_data: dict = dict()):
    
    dict_data.popitem()
    return dict_data

print(dict_hapus_data_terakhir(dict_data_siswa))
# akan mencetak {'nrp': '2002001', 'usia': 60}


# fungsi copy() digunakan untuk mengkopi objec baru dan bukan berupa reference
dict_data_baru = dict_data_siswa.copy()
dict_data_baru['alamat'] = 'Bandung'
print(dict_data_baru)
# akan mencetak {'nrp': '2002001', 'usia': 60, 'alamat': 'Bandung'}
print(dict_data_siswa)
# akan mencetak {'nrp': '2002001', 'usia': 60}


# fungsi update() digunakan untuk merubah seluruh data dictionary
dict_update = dict(baru='saja', diubah='oke')
dict_data_baru.update(dict_update)
print(dict_update)
# akan mencatak {'baru': 'saja', 'diubah': 'oke'}
