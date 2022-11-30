import string

# fungsi upper() digunakan untuk KAPITAL SELURUH karakter
# dari string, sedangkan lower sebaliknya
def upper_lower(param_text, kondisi = False):
    result = param_text.lower()
    if kondisi:
        result = param_text.upper()

    return result

print(upper_lower('yUniar', True))
# akan mencetak YUNIAR
print(upper_lower('yUNIAR'))
# akan mencetak yuniar


# fungsi capitalize() untuk KAPITAL hanya karakter pertama saja
# fungsi title() untuk KAPITAL karakter pertama pada setiap kata
# fungsi swapcase() untuk upper dan lower dari setiap karakter
def cap_title_swapcase(param_text: str = str(), pilihan: int = 1):
    result = param_text.capitalize()
    if pilihan == 2:
        result = param_text.title()
    if pilihan == 3:
        result = param_text.swapcase()
    
    return result

print(cap_title_swapcase('Kkn Di desA peNari', 1))
# akan mencetak Kkn di desa penari
print(cap_title_swapcase('Kkn Di desA peNari', 2))
# akan mencetak Kkn Di Desa Penari
print(cap_title_swapcase('Kkn Di desA peNari', 3))
# akan mencetak kKN dI DESa PEnARI


# fungsi split(<karakter_pemisah>) digunakan untuk memecah string
# berdasarkan karakter_pemisah. Hasil return berupa list
def split_string(param_text: str = str(), param_pemisah: str = str()):
    result = param_text.split(param_pemisah)
    return result

print(split_string('Serang-Jakarta-Bandung-Semarang-Yogyakarta-Surabaya','-'))
# akan mencetak ['Serang', 'Jakarta', 'Bandung', 'Semarang', 'Yogyakarta', 'Surabaya']
print(split_string('Serang:Jakarta:Bandung:Semarang:Yogyakarta:Surabaya',':'))
# akan mencetak ['Serang', 'Jakarta', 'Bandung', 'Semarang', 'Yogyakarta', 'Surabaya']


# fungsi strip(), lstrip(), rstrip() digunakan untuk menghapus karakter spasi
def strip_lstrip_rstrip(param_text: str = str(), pilihan: int = 1):
    result = ""
    if pilihan == 1:
        result = param_text.strip()
    elif pilihan == 2:
        result = param_text.rstrip()
    else:
        result = param_text.lstrip()

    return result

print(strip_lstrip_rstrip('  Kota Bandung  ', 1))
# akan mencetak Kota Bandung dengan menghilangkan spasi di kiri dan kanan string
print(strip_lstrip_rstrip('  Kota Bandung  ', 2))
# akan mencetak Kota Bandung dengan menghilangkan spasi di kanan string
print(strip_lstrip_rstrip('  Kota Bandung  ', 3))
# akan mencetak Kota Bandung dengan menghilangkan spasi di kiri string


# fungsi replace(<karakter_pencari>,<karakter_pengganti>)
def replace_text(param_text: str = str()):
    result = param_text.replace('-',':')
    return result

print(replace_text('Serang-Jakarta-Bandung'))
# akan mencetak Serang:Jakarta:Bandung


# fungsi startswith(<karakter>), endswith(<karakter>) digunakan pengecekan
# kata dari setiap string
def start_end_with_param_text(param_text: str = str(),
                              pilihan: int = int(),
                              cari_text: str = str()):
    
    result = True
    if pilihan == 1:
        result = param_text.startswith(cari_text)
    else:
        result = param_text.endswith(cari_text)

    return result

print(start_end_with_param_text('Hello World', 1, 'Hello'))
# akan mencetak True
print(start_end_with_param_text('Hello World', 1, 'Hel'))
# akan mencetak True
print(start_end_with_param_text('Hello World', 1, 'hello'))
# akan mencetak False
print(start_end_with_param_text('Hello World', 2, 'World'))
# akan mencetak True
print(start_end_with_param_text('Hello World', 2, 'WoRld'))
# akan mencetak False


# fungsi reversed() digunakan untuk membalik string dengan return berupa list
def reversed_text(param_text: str = str()):
    tmp_result = reversed(param_text)
    result = ''.join(tmp_result)
    return result

print(reversed_text("BANDUNG"))
# akan mencetak GNUDNAB


# fungsi string.xxx dapat digunakan untuk generate alphabet, string number
def string_built_in(pilihan: int = 1):
    result = ""

    if pilihan == 1:
        result = string.ascii_letters
    elif pilihan == 2:
        result = string.ascii_uppercase
    elif pilihan == 3:
        result = string.ascii_lowercase
    else:
        result = string.digits

    return result

print(string_built_in(1))
# akan mencetak string abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string_built_in(2))
# akan mencetak string ABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string_built_in(3))
# akan mencetak string abcdefghijklmnopqrstuvwxyz
print(string_built_in(4))
# akan mencetak string 0123456789


# fungsi count(<karakter>) digunakan untuk mencari berapa banyak karakter
# yang terdapat pada string. return berupa integer
def count_text(param_text: str = str(),
               param_cari: str = str()):
    tmp_count = param_text.count(param_cari)

    return tmp_count


print(count_text('SHE SELLS SEASHELLS BY THE SEAHORSE','SEA'))
# akan mencetak sebanyak 2 dikarenakan
