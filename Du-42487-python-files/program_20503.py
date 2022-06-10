def swap_keys_values(swap_me):
    o = list({swap_me[key] : key for key in list(swap_me.keys())}.items())
    o.sort(key=lambda x: x[0])
    print(o)


def main():
    swap_keys_values({1:2, 'test': 'rest'})

if __name__ == '__main__':
    main()
