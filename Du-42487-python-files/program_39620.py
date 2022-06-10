def count_letters(s):
    n = 0
    print(n)
    if not s:
        return 0
        
    else:
        n += 1
        print(n)
        return n + count_letters(s[1:])