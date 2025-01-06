""" 
                            Task
    1. Mencetak jumlah dari kedua angka (penjumlahan).
    2. Mencetak selisih dari kedua angka (angka pertama dikurangi angka kedua).
    3. Mencetak hasil kali dari kedua angka.

 """



if __name__ == '__main__':
    a = int(input())
    b = int(input())
    
    #proses pembuatan program
    def call(a,b):
        return a + b, a - b, a * b
        
    #output
    callFunction = call(a,b)
    print(callFunction[0])
    print(callFunction[1])
    print(callFunction[2])


 
    #!   ilmu yang aku dapatkan dari program ini
        # * 1 Apabila kita mengembalikan nilai dengan banyak operasi seperti di bawah kita tinggal satukan dan pisahkan dengan tanda { , }
        
        # TODO - return a + b, a - b, a * b akan menjadi sebuah tuple() apabila kita memanggilnya seperti:
        #           - print(callFunction[0]) -> ini untuk koma pertama 2 + 2 = 4 
        #           - print(callFunction[1]) -> ini untuk koma kedua 2 - 2 = 0
        #           - print(callFunction[2]) -> ini untuk koma ketiga 2 * 2 = 4 
        #           - Mejadi tuple(4,0,4)
