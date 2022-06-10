def swap_keys_values(swap_me):
    if swap_me is not None:
        return {swap_me[key] : key for key in list(swap_me.keys())}


def main():
    swap_keys_values({1:2, 'test': 'rest'})

if __name__ == '__main__':
    main()
