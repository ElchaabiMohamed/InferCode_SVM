def swap_unique_keys_values(d):
    d2 = {}
    values = list(d.values())
    sort = sorted(d.items())
    d2 = [(v,k) for (k,v) in sort if values.count(v) == 1]
    print(d2)
    

def main():
    d = {1:'one', 2:'two', 3:'one', 4:'four'}
    swap_unique_keys_values(d)

if __name__ == "__main__":
    main()