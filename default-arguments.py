# Kelas untuk menghasilkan angka genap secara berturut-turut
class EvenStream:
    def __init__(self):
        self.current = 0  # Nilai awal angka genap adalah 0

    def get_next(self):
        value = self.current  # Simpan angka genap saat ini
        self.current += 2  # Tambahkan 2 untuk mendapatkan angka genap berikutnya
        return value  # Kembalikan angka genap saat ini


# Kelas untuk menghasilkan angka ganjil secara berturut-turut
class OddStream:
    def __init__(self):
        self.current = 1  # Nilai awal angka ganjil adalah 1

    def get_next(self):
        value = self.current  # Simpan angka ganjil saat ini
        self.current += 2  # Tambahkan 2 untuk mendapatkan angka ganjil berikutnya
        return value  # Kembalikan angka ganjil saat ini


# Fungsi untuk mencetak angka dari stream tertentu
def print_from_stream(n, stream=None):
    # Jika stream tidak diberikan, gunakan EvenStream secara default
    if stream is None:
        stream = EvenStream()
    # Cetak n angka dari stream
    for _ in range(n):
        print(stream.get_next())


# Pemrosesan input untuk menjalankan program sesuai dengan soal
queries = int(input())  # Membaca jumlah query dari input
for _ in range(queries):
    stream_name, n = input().split()  # Membaca nama stream dan jumlah angka yang diminta
    n = int(n)  # Konversi jumlah angka menjadi integer
    if stream_name == "even":
        # Jika stream_name adalah "even", gunakan EvenStream
        print_from_stream(n)
    elif stream_name == "odd":
        # Jika stream_name adalah "odd", gunakan OddStream
        print_from_stream(n, OddStream())
