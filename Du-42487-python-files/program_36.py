def swap_unique_keys_values(swap_me):
    if swap_me is not None:
        d = {swap_me[key] : key for key in list(set(swap_me.keys())) if swap_me[key]}


def main():
    swap_unique_keys_values({1:2, 'test': 'rest'})

if __name__ == '__main__':
    main()
