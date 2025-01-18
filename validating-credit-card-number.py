"""
 Kamu dan Fredrick adalah teman baik. Kemarin, Fredrick menerima beberapa kartu kredit dari Bank ABCD. Dia ingin memastikan apakah nomor kartu kreditnya valid atau tidak. Karena kamu hebat dalam penggunaan regex (regular expression), Fredrick meminta bantuanmu!

Kartu kredit yang valid dari Bank ABCD harus memenuhi kriteria berikut:

* Harus dimulai dengan angka 4, 5, atau 6.
* Harus terdiri dari tepat 16 digit.
* Hanya boleh terdiri dari angka (0-9).
* Boleh memiliki angka dalam kelompok 4 digit yang dipisahkan oleh satu tanda hubung "-" (contoh: 1234-5678-9012-3456).
* Tidak boleh menggunakan pemisah lain seperti spasi (' ') atau garis bawah ('_').
* Tidak boleh memiliki 4 atau lebih angka yang sama secara berurutan (contoh: 1111 tidak diperbolehkan).

! Tugasmu adalah menulis program untuk memeriksa apakah nomor kartu kredit Fredrick valid berdasarkan aturan-aturan di atas. 😊 
"""
import re

def is_valid_credit_card(card_number):
    # Regex untuk memeriksa kartu kredit sesuai kriteria
    pattern = r'^[456]\d{3}(-?\d{4}){3}$'
    
    # Memeriksa apakah nomor kartu sesuai dengan pola regex
    if re.match(pattern, card_number):
        # Memeriksa apakah ada empat digit berturut-turut yang sama
        card_number = card_number.replace('-', '')  # Menghapus tanda penghubung '-'
        for i in range(len(card_number) - 3):
            if card_number[i] == card_number[i+1] == card_number[i+2] == card_number[i+3]:
                return "Invalid"  # Ada empat angka berturut-turut yang sama
        
        return "Valid"  # Kartu kredit valid
    else:
        return "Invalid"  # Tidak valid jika tidak sesuai pola regex

# Tes dengan beberapa input
test_cases = [
    "4123456789123456",         # Valid
    "5123-4567-8912-3456",      # Valid
    "61234-567-8912-3456",      # Invalid (format tidak sesuai)
    "4123356789123456",         # Invalid (empat digit berturut-turut sama)
    "5133-3367-8912-3456",      # Invalid (empat digit berturut-turut sama)
    "5123 - 3567 - 8912 - 3456" # Invalid (spasi tidak diperbolehkan)
]

# Menampilkan hasil untuk setiap tes
for card in test_cases:
    print(is_valid_credit_card(card))












# ilmu baru yang di dapat di soal berikut
#  penggunaan replace('-','') contoh 
# x = 1-2-3-4-5
# dengan menggunaa kan replace ('-','') :
# ! sebelumnya before 1-2-3-4-5 ----> after 1,2,3,4,

