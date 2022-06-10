def count_letters(s):
    if not s:
        return count_letters.count
    s = s[:-1]
    count_letters.count += 1
    try:
        return count_letters(s)
    finally:
        count_letters.count = 0
count_letters.count = 0