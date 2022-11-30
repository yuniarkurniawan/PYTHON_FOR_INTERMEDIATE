__author__ = 'Yuniar Kurniawan \
    2022 November 18'


from operator import itemgetter


class ListFunction:
    def __init__(self, data_list: list = list()) -> None:
        self.data_list = data_list

    # fungsi append akan menyisipkan elemen pada elemen terakhir
    def append_function(self, data_append: str = str()):
        self.data_list.append(data_append)
        return self.data_list

    # fungsi insert(<indeks>,<elemen>) digunakan untuk menyisipkan elemen
    # pada indeks tertentu
    def insert_function(self, data_indeks: int = int(),
                        data_insert: str = str()):
        self.data_list.insert(data_indeks, data_insert)
        return self.data_list

    def extend_function(self, data_exetend: list = list()):
        self.data_list.extend(data_exetend)
        return self.data_list

    def len_function(self):
        return len(self.data_list)

    # fungsi max(<data_list>) harus satu tipe data
    def max_function(self):
        return max(self.data_list)

    # fungsi min(<data_list>) harus satu tipe data
    def min_function(self):
        return min(self.data_list)

    # fungsi remove(<elemen>) harus dicek terlebih dahulu apakah eksis 
    # atau tidak, jika tidak ada maka akan error 
    def remove_function(self, data_remove):
        if data_remove in self.data_list:
            self.data_list.remove(data_remove)
        return self.data_list

    # fungsi pop(<indeks:optional>) secara default akan menghapus
    # pada indeks terakhir list
    def pop_function(self, indeks_pop):
        self.data_list.pop(indeks_pop)
        return self.data_list

    def filter_even_odd_function(self, condition):
        if condition:
            return [val for val in self.data_list if val % 2 == 0]
        else:
            return [val for val in self.data_list if val % 2 == 1]

    def filter_even_odd_lambda_function(self, condition):
        if condition:
            return list(filter(lambda val: val % 2 == 0, self.data_list))
        else:
            return list(filter(lambda val: val % 2 == 1, self.data_list))

    def sort_ascending_descending_function(self, condition):
        if condition:
            self.data_list.sort()
            return self.data_list
        else:
            self.data_list.sort(reverse=True)
            return self.data_list

    def duplicate_element_remove_function(self):
        set_data = set(self.data_list)
        return list(set_data)

    def count_function(self, element_value):
        count_value = self.data_list.count(element_value)
        return count_value

    def print_with_map_upper(self):
        upper_list = map(lambda val: val.upper(), self.data_list)
        return list(upper_list)

    def sort_ascending_descending_of_dict(self):
        self.data_list.sort(key=lambda item: item['usia'])
        return self.data_list

    def sort_ascending_descending_of_dict_using_itemgetter(self):
        by_usia = itemgetter('usia')
        self.data_list.sort(key=by_usia)
        return self.data_list
