# 1. ========== DASAR
def cetak_nama(nama): #nama merupakan paramter
    print(f'Nama saya : {nama}')

cetak_nama('Yuniar') #Yuniar merupakan argumen
# akan mencetak 'Nama saya : Yuniar'


# 2. ========== DASAR
# POSITION ARGUMEN
def cetak_bilangan(a, b, c): # multi parameter
    print(a, b, c)

cetak_bilangan(1, 2, 3)
# akan mencetak 1, 2, 3


# 3. ========== DASAR
# KEY ARGUMEN
def cetak_bilangan_dua(a, b, c): # multi parameter
    print(a, b, c)

cetak_bilangan_dua(b=1, c=2, a=3) # key argumen
# akan mencetak 3, 1, 2

# try:
#     cetak_bilangan_dua(1, b=2, 3)
# except Exception as e:
#     raise e
# akan mencetak SyntaxError: positional argument follows keyword argument
# tidak diperkenankan key argumen seperti diatas

# try:
#     cetak_bilangan_dua(1, b=2, a=3)
# except Exception as e:
#     raise e
# akan mencetak TypeError: cetak_bilangan_dua() got multiple values for argument 'a'
# karena nilai a sudah diberikan di awal = 1


# 4. ========== DASAR
# KEY WORD DENGAN DEFAULT VALUE
def cetak_bilangan_tiga(a, b, c, d=8):
    print(a, b, c, d)

cetak_bilangan_tiga(a=5, b=6, c=7)
# akan mencetak 5, 6, 7, 8


# 5. ========== DASAR
# VARIABLE LENGTH PARAMETER
# *args akan diperlaukan sebagai tuple
# **kwargs akan diperlakukan sebagai dictionary
# POSISI VARIABLE LENGTH PARAMETER harus selalu (<normal_var>,<tuple_var>,<dictionary_var>)
def cetak_bilangan_empat(a, b, *args, **kwargs): 
    print(a, b)
    print(f'---------')
    for val in args:
        print(val)
    print(f'---------')
    for key, val in kwargs.items():
        print(key, " : ",val)

# a = 1
# b = 2
# *args akan diisi dengan 3, 4, 5
# *kwargs akan diisi dengan dictionary {'enam':6, 'tujuh':7} 
cetak_bilangan_empat(1, 2, 3, 4, 5, enam=6, tujuh=7)
# akan mencetak
# 1, 2
# ---------
# 3
# 4
# 5
# ---------
# enam  :  6
# tujuh  :  7


# a = 1
# b = 2
# *kwargs akan diisi dengan dictionary {'enam':6, 'tujuh':7} 
cetak_bilangan_empat(1, 2, enam=6, tujuh=7)
# akan mencetak
# 1, 2
# ---------
# ---------
# enam  :  6
# tujuh  :  7

# a = 1
# b = 2
# *args akan diisi dengan 3, 4, 5
cetak_bilangan_empat(1, 2, 6, 7)
# akan mencetak
# 1, 2
# ---------
# 6
# 7
# ---------


def cetak_bilangan_lima(a, b, *, c, d):
    print(a, b, c, d)

cetak_bilangan_lima(a=1, b=2, c=4, d= 5)
# akan mencetak 1, 2, 4, 5

# cetak_bilangan_lima(1, 2, 3, 4)
# akan mencetak error TypeError: cetak_bilangan_lima() takes 2 positional arguments but 4 were given


cetak_bilangan_lima(1, 2, d=3, c=4)
# akan mencetak 1 2 4 3



# 5. ========== DASAR
# UNPACK ARGUMEN
# LENGTH DARI VAR STRUKTUR DATA HARUS SAMA DENGAN JUMLAH PARAMETER
def cetak_bilangan_enam(a, b, c):
    print(a, b, c)

dict_data = {'a':1, 'b':2, 'c':3}
cetak_bilangan_enam(**dict_data)
# akan mencetak 1, 2, 3

list_data = [4, 5, 6]
cetak_bilangan_enam(*list_data)
# akan mencetak 4, 5, 6

tuple_data = (10, 11, 12)
cetak_bilangan_enam(*tuple_data)
# akan mencetak 10, 11, 12


# keyword global akan menyebabkan variabel number dikenal diluar fungsi
def cetak_bilangan(x):
    global number
    number = x + 5
    return number

number = 10
print(cetak_bilangan(number))
# akan mencetak 15
print(number)
# akan mencetak 15

# jika tanpa keyword global akan menyebabkan variabel number 
# diluar fungsi tidak akan mengikuti nilai hasil dari fungsi
def cetak_bilangan(x):
    number = x + 5
    return number

number = 10
print(cetak_bilangan(number))
# akan mencetak 15
print(number)
# akan mencetak 10


# jika variabel yang dilewatkan berupa tipe data struktur mutable
# maka akan diperlakukan global var
def cetak_list(my_list):
    my_list.append(10)
    return my_list

my_list = [1, 2, 3]
print(cetak_list(my_list))
# akan mencetak [1, 2, 3, 10]
print(my_list)
# akan mencetak [1, 2, 3, 10]
