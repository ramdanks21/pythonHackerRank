"""
                    ! TASK
 Kita diberikan sebuah string yang immutable (tidak dapat diubah langsung), dan kita diminta untuk melakukan perubahan pada salah satu karakter dalam string tersebut dengan karakter baru pada posisi tertentu.
Setelah itu, hasil string yang sudah diubah harus ditampilkan.

"""
def mutate_string(string, position, character):
    return string[:position] + character + string[position+1:]

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)