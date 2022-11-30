import functools

# dekorator_cetak_nama digunakan untuk menambahkan keterangan
# . Lahir di kota Bandung
def dekorator_cetak_nama(func):

    @functools.wraps(func)
    def wrapper(nama):
        tmp_nama = func(nama)
        tmp_nama = tmp_nama + ". Lahir di kota Bandung"
        return tmp_nama
    return wrapper

@dekorator_cetak_nama
def cetak_nama(nama):
    return f'Nama saya adalah {nama}'

# dekorator_cetak_bilangan_genap digunakan untuk dekorasi
# list_bilangan menjadi bilangan genap
def dekorator_cetak_bilangan_genap(func):

    @functools.wraps(func)
    def wrapper(list_bilangan = list()):
        list_bilangan_genap = [val for val in list_bilangan if val % 2 == 0]
        return list_bilangan_genap
    
    return wrapper

@dekorator_cetak_bilangan_genap
def list_bilangan(list_bilangan = list()):
    return list_bilangan


# dekorator_nama_lengkap disertia dengan parameter didalamnya
def nama_lengkap(nama_lengkap):
    def dekorator_nama_lengkap(func):
        
        @functools.wraps(func)
        def wrapper(nama):
            nama = f'{func(nama)} {nama_lengkap}'
            return nama
        return wrapper
    return dekorator_nama_lengkap


var = 'Kurniawan'
@nama_lengkap(var)
def cetak_nama_siswa(nama):
    return f'Nama : {nama}'
