def wrapper(f):
    def fun(l):
        formatted_numbers = []
        for number in l:
            #mengambil 10 digit terakhir dari nomor
            clean_number = number[-10:]
            #memformat ke bentuk "+91 xxxxx xxxxx"
            formatted_number = f"+91 {clean_number[:5]} {clean_number[5:]}"
            formatted_numbers.append(formatted_number)
        return f(formatted_numbers)
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 