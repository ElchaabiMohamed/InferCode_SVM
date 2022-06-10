d = {
    'a': 4,
    'b': 5,
    'c': 3,
    'd': 5
}

def swap_unique_keys_values(d):
    new_d = {}
    doubles = set()
    for k, v in list(d.items()):
        if v in new_d:
            doubles.add(v)
        new_d[v] = k
    for k in doubles:
        del new_d[k]
    return new_d

def main():
    swap_unique_keys_values(d)

if __name__ == '__main__':
    main()
