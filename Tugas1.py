nilai = int(input("Masukkan nilai anda :"))
usia = int(input("Masukkan Umur: "))

if nilai >= 75:
    if usia < 18:
        print("Selamat adek kamu lulus ujian")
    else :
        print("Selamat abang/kakak  kamu lulus ujian!")
else:
    if(usia < 18):
        print("Mohon maaf adek, kamu belum lulus ujia, coba lagi")
    else: 
        print("Mohon maaf abang/kakak kamu belum lulus ujian, coba lagi")

