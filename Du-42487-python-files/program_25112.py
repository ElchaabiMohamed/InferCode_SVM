def count_letters(word):
    if not word:
        return 0
    else:
        return 1 + count_letters(word[1:])


print((count_letters('car')))
