from itertools import accumulate
import operator

# fungsi accumulate digunakan untuk mengakumulasi nilai setiap elemen

list_data = [1, 2, 3, 4]
acc = accumulate(list_data)
print(f'{list(acc)}')
# akan mencetak [1, 3, 6, 10]
# dia akan menjumlahkan setiap elemen yang hasilnya disimpan sebagai elemen baru
# secara default accumulate([], <sum:default>)

acc = accumulate(list_data, func=operator.mul)
print(f'{list(acc)}')
# akan mencetak [1, 2, 6, 24]
# dia akan mengali dari setiap elemen
