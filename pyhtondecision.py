""" 
        * Program yang Anda buat harus:

Membaca dua bilangan bulat, yaitu a dan b, dari input standar.
Menampilkan dua baris hasil:
Baris pertama adalah hasil pembagian bilangan bulat (integer division) menggunakan operator //.
Baris kedua adalah hasil pembagian bilangan dengan hasil tipe float menggunakan operator /. 

"""

if __name__ == '__main__':
    a = int(input("Masukan Nilai Pertama: "))
    b = int(input("Masukan Nilai Kedua:"))

    def integerDivision(a,b):
        return a // b, a /b
    
    showData = integerDivision(a,b)
    print(showData[0])
    print(showData[1])