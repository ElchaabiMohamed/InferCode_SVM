def count_letters(n, word):
    if len(word) == 0:
        return 0
    if word[0] == n:
        count = 1
    else:
        return count + count_letters(n, word[1:])
