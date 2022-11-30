class Decorator(object):

    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print(f'------------------')
        result = self.func(*args, **kwargs)
        print(f'------------------')
        return result


@Decorator
def cetak_nama(nama):
    print(f'Nama saya : {nama}')

cetak_nama('Yuniar')
# akan mencetak 
# ------------------
# Nama saya Yuniar
# ------------------



class DecoratorBilanganGenap(object):

    def __init__(self, func):
        self.func = func

    def __call__(self, list_bilangan):
        tmp_list_result = self.func(list_bilangan)
        #result = [val for val in tmp_list_result if val % 2 == 0]
        result = list(filter(lambda val: val % 2 == 0, tmp_list_result))
        print(f'------- BILANGAN GENAP -------')
        return result
        
        

@DecoratorBilanganGenap
def cetak_bilangan(list_bilangan):
    return list_bilangan

list_bilangan = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(cetak_bilangan(list_bilangan))
# akan mencetak 
# ------- BILANGAN GENAP -------
# [2, 4, 6, 8, 10]
