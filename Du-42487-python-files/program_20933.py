def count_letters(string, count=0):
    if string == "":
        return count
    else:
        string = string[1:]
    return count_letters(string, count + 1)
