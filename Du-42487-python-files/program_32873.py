def swap_keys_values(swap_me):
    if swap_me is not None:
        o = {swap_me[key] : key for key in list(swap_me.keys())}
        o = list(o.items())
        o = list(o)
        o.sort(key=lambda x: x[0])
        print(o)


def main():
    swap_keys_values({1:2, 'test': 'rest'})

if __name__ == '__main__':
    main()
