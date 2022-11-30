# lambda arguments: expression

# 1. ============== DASAR
# versi fungsi lambda
tambah_10 = lambda bil: bil + 10
print(tambah_10(5))


# versi fungsi biasa
def tambah_10_func(bil):
    return bil + 10


print(tambah_10_func(5))


# 2. ============== DASAR
# versi lambda
isi_kubus = lambda p, l, t: p * l * t


print(isi_kubus(10, 5, 4))


# versi fungsi biasa
def isi_kubus_func(p, l, t):
    return p * l * t


print(isi_kubus_func(10, 5, 4))


# 3. ============== DASAR
# versi lambda
listing = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
bil_genap = lambda listing: [val for val in listing if val % 2 == 0]
print(bil_genap(listing))


# versi fungsi biasa
def bil_genap_func(listing):
    return [val for val in listing if val % 2 == 0]


print(bil_genap_func(listing))


# 4. ============== DASAR
# versi lambda
listing = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
bil_genap = list(filter(lambda val: val % 2 == 0, listing))
print(bil_genap)
