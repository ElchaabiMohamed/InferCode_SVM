def count_letters(s):
    number = 0
    if not s:
        return 0

    else:
        number += 1
        return number + count_letters(s[1:])