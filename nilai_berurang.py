""" 
                Soal:
Program ini akan membaca sebuah bilangan bulat 
N
N dari input. Tanpa menggunakan metode string, tugas Anda adalah mencetak angka dari 1 hingga 
N
N secara berturut-turut tanpa spasi di antara angka-angka tersebut.

Contoh:

Jika input adalah 5, output yang diharapkan adalah 12345.
Jika input adalah 10, output yang diharapkan adalah 12345678910. """


if __name__ == '__main__':
    x = int(input())
    
    for i in range(1,x+1):
     print(i, end='')

     #catatan fungsi end
     # jadi fungsi end='' di sini mengubah posisi outpu yang sebelumnya seperti:
    """     
    1
    2
    3
    4
    """

    #Menggunakan end=''
    # 1234