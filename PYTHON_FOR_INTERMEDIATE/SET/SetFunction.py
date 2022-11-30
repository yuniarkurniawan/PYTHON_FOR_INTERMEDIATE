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
