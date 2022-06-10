def count_letters(n="", i=0):
    if n == "":
        return i
    i += 1
    return count_letters(n.replace(n[0], "", 1), i)
