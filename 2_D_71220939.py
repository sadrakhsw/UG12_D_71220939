print("~~ Table Matematika Nich ~~~")
print("Pilihan model matematika")
print("1. Perkalian \n2. Pembagian")
barang = int(input("Masukkan model matematika yang diinginkan 1/2 :"))
if barang == 1:
    angka = int(input("Masukkan table matematika dari angka :"))
    for i in range(1,11):
            hasil = angka * i
            print(angka, "x", i, '=',hasil)
elif barang == 2:
    angka1 = int(input("menampilkan table matematika dengan angka :"))
    for i in range(50,66):
        hasil1 = i / angka1
        print(i, ':', angka1, '=',hasil1)
else:
    print("pilihan tidak tersedia, jangan ngasal")
