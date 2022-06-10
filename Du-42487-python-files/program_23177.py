def count_letters(s):
    if s=="":
        return 0
    a=0
    for letter in s:
        a+=1
    return a


def main():
    len = None
    print((count_letters('cat')))
    print((count_letters('catastrophe')))
    print((count_letters('')))

if __name__ == '__main__':
    main()