def swap_unique_keys_values(d):
    pairs = list(d.items())
    new_d = {}
    for key, value in pairs:
        if not value in new_d:
            new_d[value] = key
        else:
            del new_d[value]
    return new_d


def main():
    d = {'a': 4, 'b': 7, 'c': 10, 'd': 7}
    print((swap_unique_keys_values(d)))


if __name__ == '__main__':
    main()
