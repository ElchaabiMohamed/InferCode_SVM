def count_letters(word):
    if word == "":
        return 0
    return count_letters(word[:-1]) + 1
