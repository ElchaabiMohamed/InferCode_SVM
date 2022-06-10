def swap_unique_keys_values(d):
    d2 = {}
    values = list(d.values())
    print((sorted(d.items())))
   

def main():
    d = {1:'one', 2:'two', 3:'one', 4:'four'}
    swap_unique_keys_values(d)

if __name__ == "__main__":
    main()