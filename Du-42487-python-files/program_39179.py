def count_letters(s):
    if s == '':
        return 0
    l = [char for char in s.strip()]

    return 1 + count_letters(''.join(l[:-1]))