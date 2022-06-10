def swap_keys_and_values(swap_me):
    return {swap_me[key] : key for key in list(swap_me.keys())}

def main():
    print((swap_keys_and_values({1:2, 'test': 'rest'})))

if __name__ == '__main__':
    main()
