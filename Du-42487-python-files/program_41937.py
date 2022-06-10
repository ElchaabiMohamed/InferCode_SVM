def swap_unique_keys_values(d):
    return({v : k for (k,v) in list(d.items()) if list(d.values()).count(v) == 1})

def main():
    d = {1:'one', 2:'two', 3:'one'}
    swap_keys_values(d)

if __name__ == "__main__":
    main()