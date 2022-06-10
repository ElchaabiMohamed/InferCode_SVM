def count_letters(s):
    global count
    count += 1
    if not s:
        return count
    s = s[:-1]
    return count_letters(s)

count = 0