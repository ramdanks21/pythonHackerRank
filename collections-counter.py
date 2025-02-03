""" 
            Deskripsi Masalah
Raghu adalah seorang pemilik toko sepatu. Ia memiliki X pasang sepatu dengan berbagai ukuran.
Setiap pelanggan datang dengan permintaan ukuran sepatu tertentu dan harga yang bersedia mereka bayar.
Jika ukuran sepatu yang diminta tersedia, maka Raghu menjualnya dan mendapat uang sesuai harga yang ditawarkan pelanggan.
Tugas kita adalah menghitung total pendapatan yang Raghu peroleh. """

""" 
Contoh Input & Output
Input:

Copy
Edit
10
2 3 4 5 6 8 7 6 5 18
6
6 55
6 45
6 55
4 40
18 60
10 50 """

""" 
                Penjelasan:

Raghu memiliki sepatu dengan ukuran: 2, 3, 4, 5, 6, 8, 7, 6, 5, 18.
Pelanggan pertama ingin membeli sepatu ukuran 6 dengan harga 55. Raghu memiliki ukuran ini, jadi dia menjualnya dan mendapat 55.
Pelanggan kedua juga ingin ukuran 6 dengan harga 45, dan Raghu masih memiliki satu lagi, jadi dia menjualnya dan mendapat tambahan 45.
Pelanggan ketiga ingin 6 lagi, tetapi stok sudah habis, jadi tidak bisa dijual.
Pelanggan keempat membeli ukuran 4 dengan harga 40, stok tersedia, maka dia menjualnya.
Pelanggan kelima membeli ukuran 18 dengan harga 60, stok tersedia, maka dia menjualnya.
Pelanggan keenam ingin ukuran 10, tetapi tidak tersedia di stok.
Total pendapatan Raghu = 55 + 45 + 40 + 60 = 200. """

from collections import Counter

# Input jumlah sepatu yang tersedia
x = int(input())  

# Input daftar ukuran sepatu yang tersedia
shoe_sizes = Counter(map(int, input().split()))  

# Input jumlah pelanggan
n = int(input())  

total_income = 0  # Untuk menyimpan total pendapatan

for _ in range(n):
    size, price = map(int, input().split())  # Input ukuran dan harga dari pelanggan
    
    if shoe_sizes.get(size, 0) > 0:  # Pastikan ukuran tersedia
        total_income += price  # Tambahkan pendapatan
        shoe_sizes[size] -= 1  # Kurangi stok sepatu

print(total_income)  # Output total uang yang diperoleh
