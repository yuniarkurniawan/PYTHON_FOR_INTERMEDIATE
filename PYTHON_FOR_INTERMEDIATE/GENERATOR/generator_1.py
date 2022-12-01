def iterator_bilangan():
    print(f'Nilai : {0}')
    print(f'Nilai : {1}')
    print(f'Nilai : {2}')
    print(f'Nilai : {3}')

def generator_bilangan():
    yield 0
    yield 1
    yield 2
    yield 3

def utama():
    # pada fungsi iterator_bilangan semua perintah print akan dijalankan
    iterator_bilangan()
    # akan mencetak 
    # Nilai : 0
    # Nilai : 1
    # Nilai : 2
    # Nilai : 3
    # Nilai : 4
    
    # berbeda jika menggunakan yield, dia akan berhenti jika tidak
    # menggunakan perintah next(<obj_generator>)
    gen = generator_bilangan()
    print(f'Nilai : {next(gen)}')
    # akan mencetak 1 yield saja
    # Nilai : 0

utama()




def iterator_list(list_data):
    for val in list_data:
        print(f'Val : {val}')


def generator_list(list_data):  
    for val in list_data:
        yield val
        
def utama_2():
    list_data = [10, 5, 4, 7, 1, 9]
    iterator_list(list_data)
    # akan mencetak 
    # Val : 10
    # Val : 5
    # Val : 4
    # Val : 7
    # Val : 1
    # Val : 9
    # tampak disini bahwa fungsi iterator_list akan mencetak semua data list_data

    gen_list = generator_list(list_data)
    print(f'Val : {next(gen_list)}')
    # akan mencetak 
    # Val : 10
    # tampak disini hanya akan mencetak elemen ke 1 saja dan tidak akan mencetak 
    # semua list data

    print(f'Val : {next(gen_list)}')
    # akan mencetak 
    # Val : 10
    # Val : 5
    # tampak disini hanya akan mencetak elemen selanjutnya saja dan tidak akan mencetak 
    # semua list data

    # kesimpulannya fungsi generator dengan kata kunci yield
    # akan segera return tanpa mengeksekusi perintah2 dibawahnya


utama_2()


def counter_antrian(batas_antrian: int = int, antrian_saat_ini: int = int):
    global no_antrian

    # cara ini akan sangat lama dan memakan resource
    # bayangkan jika batas_antrian 1000000
    # maka akan loop sebanyak min 999999 kali
    for _ in range(1, batas_antrian):
        no_antrian += 1
        print(f'Antrian : {no_antrian}')
        if no_antrian == antrian_saat_ini:
            break


def counter_generator_antrian(batas_antrian: int = int):
    no_antrian_gen = 0
    for _ in range(1, batas_antrian):
        no_antrian_gen += 1
        yield no_antrian_gen

no_antrian = 0
batas_antrian = 10
counter_antrian(batas_antrian, 1)
# akan mencetak Antrian : 1
counter_antrian(batas_antrian, 2)
# akan mencetak Antrian : 2


count_gen = counter_generator_antrian(batas_antrian)
print(f'Antrian : {next(count_gen)}')
# akan mencetak Antrian : 1
print(f'Antrian : {next(count_gen)}')
# akan mencetak Antrian : 2
# dst selama menggunakan next(<obj_generator>)
