def count_letters(item, length = 0):
    try:
        item[0]
    except IndexError:
        return length

    item = item[1:]

    length += 1

    return count_letters(item, length)


def main():
    len = None
    print((count_letters('cat')))
    print((count_letters('catastrophe')))
    print((count_letters('')))

if __name__ == '__main__':
    main()
