def count_letters(s):
    if not s:
        return count_letters.count
    s = s[:-1]
    count_letters.count += 1
    return count_letters(s)

count_letters.count = 0