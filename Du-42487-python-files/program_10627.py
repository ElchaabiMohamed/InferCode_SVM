def count_letters(w):
    if w == "":
        return 0

    return 1 + count_letters(w[1:])

