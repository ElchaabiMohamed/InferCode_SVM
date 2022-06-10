def swap_unique_keys_values(d):

    values = list(d.values())
    l = [(v,k) for (k,v) in list(d.items()) if values.count(v) == 1]
    print((sorted(l)))
    

def main():
    d = {1:'one', 2:'two', 3:'one', 4:'four'}
    swap_unique_keys_values(d)

if __name__ == "__main__":
    main()