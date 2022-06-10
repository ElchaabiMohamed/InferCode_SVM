def count_letters(s):
    if len(s) == 0:
        return 0

    s = list(s)
    s.remove(s[0])
    return 1 + count_letters(s)

def main():
    len = None
    print((count_letters('cat')))
    print((count_letters('catastrophe')))
    print((count_letters('')))

if __name__ == '__main__':
    main()