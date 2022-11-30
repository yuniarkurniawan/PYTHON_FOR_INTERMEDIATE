import copy

# penggunaan fungsi copy() pada list digunakan untuk menciptakan objek 
# baru pada list_baru
def cetak_list(list_data: list = []):
    list_baru = list_data.copy()
    list_baru.append(6)
    list_baru.append(7)
    return list_baru

list_data = [1, 2, 3, 4, 5]
print(cetak_list(list_data))
# akan mencetak [1, 2, 3, 4, 5, 6, 7]
print(list_data)
# akan mencetak [1, 2, 3, 4, 5]


# jika tidak menggunakan copy() atau hanya sebatas reference 
# maka akan merubah nilai parentnya 
# baru pada list_baru
def cetak_list_dua(list_data: list = []):
    list_baru = list_data
    list_baru.append(6)
    list_baru.append(7)
    return list_baru

list_data = [1, 2, 3, 4, 5]
print(cetak_list_dua(list_data))
# akan mencetak [1, 2, 3, 4, 5, 6, 7]
print(list_data)
# akan mencetak [1, 2, 3, 4, 5, 6, 7]


# fungsi copy.deepcopy() dapat digunakan untuk mengcopy list bersarang
def cetak_list_tiga(data_list: list = []):
    list_baru = copy.deepcopy(data_list)
    list_baru.append([7, 8])
    return list_baru

list_data_multiple = [[1, 2], [3, 4], [5, 6]]
print(cetak_list_tiga(list_data_multiple))
# akan mencetak [[1, 2], [3, 4], [5, 6], [7, 8]]
print(list_data_multiple)
# akan mencetak [[1, 2], [3, 4], [5, 6]]
