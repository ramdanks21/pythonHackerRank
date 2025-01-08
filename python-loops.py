"""
     Program yang harus Anda buat:

Membaca sebuah bilangan bulat positif N dari input standar (STDIN).
Untuk setiap bilangan bulat non-negatif i yang memenuhi syarat i < N, cetak nilai i^2 (kuadrat dari i) pada baris baru.
 """

if __name__ == '__main__':
    n = int(input())
    i = 0
    while i < n: # nilai i kurang dari nilai n / nilai yang di inputkan user
        
      if n >= 0: # jika nila N >= 0 kita tampilkan nilai bilangan bulat positif  pangkat 2
        print(i ** 2)
        i+=1
      else:
         print(f'Nilainya {n}')


#catatana

#  