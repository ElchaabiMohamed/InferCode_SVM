def swap_keys_and_values(swap_me):
    print((list({swap_me[key] : key for key in list(swap_me.keys())}.items())))

def main():
    swap_keys_and_values({1:2, 'test': 'rest'})

if __name__ == '__main__':
    main()
