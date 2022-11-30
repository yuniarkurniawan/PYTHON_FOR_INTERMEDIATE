from collections import OrderedDict
import json
import functools

# pada dekorator ini dicontohkan penggunaan dekorator dengan melewatkan argumen


DICT_MATA_KULIAH = OrderedDict()
DICT_MATA_KULIAH = [
    {
        "id": 1,
        "nama_mata_kuliah": "Pemograman Python",
        "sks": 4
    },
    {
        "id": 2,
        "nama_mata_kuliah": "Sistem Terdistribusi",
        "sks": 3
    },
    {
        "id": 3,
        "nama_mata_kuliah": "Pemograman OOP",
        "sks": 3
    },
    {
        "id": 4,
        "nama_mata_kuliah": "Jaringan",
        "sks": 2
    },
    {
        "id": 5,
        "nama_mata_kuliah": "Algoritma",
        "sks": 3
    },
    {
        "id": 6,
        "nama_mata_kuliah": "Aljabar",
        "sks": 4
    },
]


def mata_kuliah_pilihan(list_pilihan: list = []):

    def dekorator_data_dosen(func):

        @functools.wraps(func)
        def wrapper(data_dosen: dict = OrderedDict()):

            list_mata_kuliah = []
            for val in list_pilihan:
                for key, val_dict in enumerate(DICT_MATA_KULIAH):
                    if val_dict.get("id") == val:
                        dict_dosen_mata_kuliah = OrderedDict()
                        dict_dosen_mata_kuliah = DICT_MATA_KULIAH[key].copy()
                        list_mata_kuliah.append(dict_dosen_mata_kuliah)
                        DICT_MATA_KULIAH.pop(key)

            data_dosen['mata_kuliah'] = 'Belum memilikia mata kuliah'
            if len(list_mata_kuliah) > 0:
                data_dosen['mata_kuliah'] = list_mata_kuliah
            hasil = func(data_dosen)
            return hasil

        return wrapper

    return dekorator_data_dosen


list_dosen_mata_kuliah = [1, 3, 6]


@mata_kuliah_pilihan(list_dosen_mata_kuliah)
def cetak_json_data_dosen(data_dosen: dict = OrderedDict()):
    dosen_json = json.dumps(data_dosen)
    return dosen_json
