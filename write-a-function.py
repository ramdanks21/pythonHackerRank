"""     
                             TASK
        Tahun kabisat:
        * Harus dapat dibagi habis dengan 4 (tanpa sisa).
        * Jika dapat dibagi habis dengan 100, tidak kabisat kecuali juga dapat dibagi habis dengan 400. """
def is_leap(year):  # Fungsi untuk menentukan apakah suatu tahun adalah tahun kabisat
    # Tidak ada kebutuhan awal untuk inisialisasi variabel karena semua kondisi langsung di-return

    # Langkah 1: Periksa apakah tahun habis dibagi 400
    if year % 400 == 0:  
        # Jika habis dibagi 400, tahun ini adalah tahun kabisat
        return True  

    # Langkah 2: Jika tidak habis dibagi 400, periksa apakah habis dibagi 100
    elif year % 100 == 0:  
        # Jika habis dibagi 100 tapi tidak habis dibagi 400, maka bukan tahun kabisat
        return False  

    # Langkah 3: Jika tidak habis dibagi 100, periksa apakah habis dibagi 4
    elif year % 4 == 0:  
        # Jika habis dibagi 4 tapi tidak habis dibagi 100, maka ini tahun kabisat
        return True  

    # Langkah 4: Jika tidak memenuhi semua kondisi di atas, maka bukan tahun kabisat
    # Secara implisit, kondisi ini akan mengembalikan False karena tidak ada return lain
    # Tidak perlu menuliskan kondisi eksplisit untuk False
    # Semua nilai tahun yang tidak memenuhi salah satu dari kondisi di atas akan dikembalikan False

# Meminta input dari pengguna
year = int(input())  # Input dari pengguna diubah menjadi bilangan bulat
print(is_leap(year))  # Menjalankan fungsi dan mencetak hasilnya (True atau False)
