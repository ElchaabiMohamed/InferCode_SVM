def count_letters(s, i=0):
    if s != "":
        i+=1
        return count_letters(s[1:], i)
    else:
        return i
