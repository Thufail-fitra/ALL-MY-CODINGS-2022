def segitiga():
    alas = float(input("Masukan alas segitiga: "))
    tinggi = float(input("Masukan tinggi segitiga: "))
    luas = 0.5 * alas * tinggi
    print("Luas Segitiga : "+str(luas))
    return luas

def segitiga2():
    sisi1 = float(input("Masukan sisi 1 segitiga: "))
    sisi2 = float(input("Masukan sisi 2 segitiga: "))
    sisi3 = float(input("Masukan sisi 3 segitiga: "))
    keliling = sisi1 + sisi2 + sisi3
    print("Keliling Segitiga : ", keliling)
    return keliling

while True:
    print("===== SELAMAT DATANG DI PROGRAM Segitiga =====")
    print("Berikut Menu yang tersedia:")
    print("1. Mencari Luas Segitiga")
    print("2. Mencari Keliling Segitiga")
    print("3. Tutup")
    option = input("Option 1-3 : ")
    if option == "1":
        print("Anda Pilih Menu 1")
        segitiga()
    elif option == "2":
        print("Anda Pilih Menu 2")
        segitiga2()
    elif option == "3":
        break
    else:
        print("Keyword Anda salah coba ulang lagi!!!")