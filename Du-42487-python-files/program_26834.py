def swap_unique_keys_values(d):
    d2 = {}
    values = list(d.values())

    for (k,v) in list(d.items()):
        if values.count(v) == 1:
            d2[v] = k
    print(d2)
    

def main():
    d = {1:'one', 2:'two', 3:'one'}
    swap_unique_keys_values(d)

if __name__ == "__main__":
    main()