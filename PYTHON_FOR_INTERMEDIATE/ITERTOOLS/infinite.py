from itertools import count, repeat, cycle

# fungsi itertools count(n) digunkan untuk looping dimulai dari n
# dan terus mengulan tanpa henti
# untuk menghentikannya dapat menggunakan break condition

for i in count(10):
    print(i)

    # jika tidak menggunakan baris perintah dibawah ini
    # maka akan loop terus menerus
    # perintah dibawah ini akan menghentikan jika i sudah = 15
    if i == 15:
        break



# fungsi itertool cycle(<list>) digunakan untuk mencetak
# berulang tanpa henti dan terus menerus

list_data = [1, 2, 3]
for val in cycle(list_data):
    print(val)

    # jika tidak diberikan perintah break maka akan terus mencetak
    # 1
    # 2
    # 3
    # secara terus menerus
    # untuk menghentikannya gunakan perintah if break
    if val == 3:
        break


# for i in repeat(1):
#     print(i)

    # akan mencetak secara terus menerus angka 1


for i in repeat(3, 2):
    print(i)
    # akan mencetak secara terus menerus angka 3 dan akan berhenti setelah
    # 3x pengulangan