def swap_keys_values(d):
    d = ({v: k for k,v in list(d.items())})
    print((list(d.items())))


def main():
    d = {"a": 4, "b" : 7, "c" : 10}
    swap_keys_values(d)

if __name__ == '__main__':
    main()