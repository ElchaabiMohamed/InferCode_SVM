def swap_keys_values(d):
    return({k : v for (v,k) in list(d.items())})

def main():
    d = {1:'one', 2:'two'}
    swap_keys_values(d)

if __name__ == "__main__":
    main()