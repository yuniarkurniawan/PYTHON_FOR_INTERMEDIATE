__author__ = 'Yuniar Kurniawan \
    2022 November 18'


class SetFunction:
    def __init__(self, data_set_bilangan_satu: set = set(),
                 data_set_bilangan_dua: set = set()) -> None:
        self.data_set_bilangan_satu = data_set_bilangan_satu
        self.data_set_bilangan_dua = data_set_bilangan_dua

    # fungsi intersection digunakan untuk mencari irisan
    # dari kedua atau lebih set
    def intersection_function(self):
        set_intersection = self.data_set_bilangan_satu.\
            intersection(self.data_set_bilangan_dua)
        return set_intersection

    # fungsi union digunakan untuk menggabungkan kedua set
    def union_function(self):
        set_union = self.data_set_bilangan_satu.\
            union(self.data_set_bilangan_dua)
        return set_union

    # fungsi difference digunakan untuk mencari elemen berbeda dari set
    # sebelah kiri
    def difference_function(self):
        set_difference = self.data_set_bilangan_satu.\
            difference(self.data_set_bilangan_dua)
        return set_difference

    # fungsi symmetric_difference digunakan untuk mencari
    # elemen berbeda dari set
    # sebelah kiri dan kanan
    def symmetric_difference_function(self):
        set_symmetrict_difference = self.data_set_bilangan_satu.\
            symmetric_difference(self.data_set_bilangan_dua)
        return set_symmetrict_difference

    # fungsi copy digunakan untuk mencipatakan objek baru dengan nilai
    # set baru
    def copy_function(self):
        set_copy = self.data_set_bilangan_satu.copy()
        return set_copy

    # fungsi discard() digunakan untuk menghapus elemen dari suatu set
    def discard_function(self, elemen_hapus):
        self.data_set_bilangan_satu.discard(elemen_hapus)
        return self.data_set_bilangan_satu

    # fungsi isdisjoint akan mengembalikan nilai boolean. Jika terdapat satu
    # kesamaan saja maka akan bernilai False
    def isdisjoint_function(self):
        set_isdisjoint = self.data_set_bilangan_satu.\
            isdisjoint(self.data_set_bilangan_dua)
        return set_isdisjoint

    # fungsi issubset akan mengembalikan nilai boolean.
    # Jika seluruh elemen set kiri
    # berada pada set sebelah kanan maka akan bernilai True,
    # begitupun sebaliknya
    def issubset_function(self):
        set_issubset = self.data_set_bilangan_satu.\
            issubset(self.data_set_bilangan_dua)
        return set_issubset

    # fungsi isupperset akan mengembalikan nilai boolean.
    # Jika sebagian dari elemen set kiri
    # terdapat pada set sebelah kanan akan bernilai True, begitupu sebaliknya
    def issuperset_function(self):
        set_issuperset = self.data_set_bilangan_satu.\
            issuperset(self.data_set_bilangan_dua)
        return set_issuperset
