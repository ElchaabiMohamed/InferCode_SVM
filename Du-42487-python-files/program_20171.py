def count_letters(word, current=0):
    if word == "":
        return current
    return count_letters(word[1:], current = current + 1)
