
# Berikut adalah penjelasan lengkap mengenai program yang menghitung Produk Kartesius dari dua daftar bilangan bulat menggunakan for loop, beserta penjelasan detail dalam programnya.

# Problem (Masalah yang Diberikan)
# Kita diberikan dua daftar bilangan bulat unik yang sudah terurut, yaitu daftar A dan B. Tugas kita adalah menghitung produk Kartesius dari kedua daftar tersebut.

# Produk Kartesius
# Produk Kartesius adalah semua kemungkinan pasangan elemen antara dua daftar, yaitu:

# Input daftar A dan B
A = [1,2,3]
B = [4,5,6]

# Hitung Produk Kartesius menggunakan for loop
for a in A:
    for b in B:
            print(f"({a}, {b})", end=" ")
            






"""
            Ilmu yang didapatkan 
 input() → Mengambil input dari pengguna dalam bentuk string.
.split() → Memisahkan input berdasarkan spasi sehingga menghasilkan daftar string.
map(int, ...) → Mengonversi setiap elemen string menjadi bilangan bulat.
list(...) → Mengubah hasil konversi menjadi daftar bilangan bulat. 
end=" " -> agar tulisan dcode ke samping bukan ke bawah
"""