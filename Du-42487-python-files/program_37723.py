def count_letters(s):
    n = 0
    if not s:
        return 0
    
    else:
        n += 1
        return n + count_letters(s[1:])

def main():
    len = None
    print((count_letters('cat')))
    print((count_letters('catastrophe')))
    print((count_letters('')))

if __name__ == '__main__':
    main()
