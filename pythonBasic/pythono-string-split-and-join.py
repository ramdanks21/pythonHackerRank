
# Membuat sebuah string split and join
#ouptu diharapkan this-is-a-string
def split_and_join(line):
    # write your code here
    return "-".join(line.split())

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)