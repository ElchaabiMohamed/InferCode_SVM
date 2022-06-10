def swap_keys_values(d):
    pairs = list(d.items())
    new_d = {}
    for key, value in pairs:
        new_d[value] = key
    return new_d


def main():
    d = {'a': 1, 'b': 2, 'c': 3}
    print((swap_keys_values(d)))


if __name__ == '__main__':
    main()
