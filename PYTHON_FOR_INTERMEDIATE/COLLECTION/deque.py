from collections import deque

# deque dapat diperlakukan seperti LIST

data_deque = deque('EFGHIJKL')
print(f'Data deque : {data_deque}')
# akan mencetak deque(['E','F', 'G', 'H', 'I', 'J', 'K', 'L'])

# untuk iterasi bisa menggunakan for loop
for val in data_deque:
    print(f'Data deque lower : {val.lower()}')
# akan mencetak 
# Data deque lower : e
# Data deque lower : f
# Data deque lower : ... dst
# Data deque lower : l

# fungsi appendleft(<elemen>) dan append(<elemen>)
data_deque.append('M')
print(f'Setelah append() : {data_deque}')
# akan mencetak Setelah append() : deque(['E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M'])

data_deque.appendleft('D')
print(f'Setelah appendleft() : {data_deque}')
# akan mencetak Setelah appendleft() : deque(['D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M'])


# penggunaan fungsi extend() dan extendleft() 
data_deque.extend(['N', 'O'])
print(f'Setelah extend() {data_deque}')
# akan mencetak Setelah appendleft() : deque(['D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O'])

data_deque.extendleft(['B', 'C'])
print(f'Setelah extendleft() {data_deque}')
# akan mencetak etelah extendleft() deque(['C', 'B', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O'])

# fungsi pop() digunakan untuk menghapus elemen terakhir
data_deque.pop()
print(f'Setelah proses pop() {data_deque}')
# akan mencetak Setelah proses pop() deque(['C', 'B', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N'])

# fungsi popleft() digunakan untuk menghapus elemen pertama
data_deque.popleft() 
print(f'Setelah fungsi popleft() {data_deque}')
# akan mencetak Setelah fungsi popleft() deque(['B', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N'])


# fungsi rotate(<n>) digunakan untuk menggeser ke kiri/kanan n kali
data_deque.rotate(2)
print(f'Setelah fungsi rotate(+) {data_deque}')
# akan mencetak Setelah fungsi rotate() deque(['M', 'N', 'B', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L'])
# setiap elemen akan tergeser ke kanan sebanyak 2 step

data_deque.rotate(-4)
print(f'Setelah fungsi rotate(-) {data_deque}')
# akan mencetak Setelah fungsi rotate() deque(['E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'B', 'D'])
# setiap elemen akan tergeser ke kiri sebanyak 4 step
