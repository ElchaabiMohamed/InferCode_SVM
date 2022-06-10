def swap_unique_keys_values(d):
    values = list(d.values())
    items = list(d.items())
    l = {v : k for (k,v) in items if values.count(v) == 1}
    return(sorted(l))

def main():
    d = {'one':1, 'two':2, 'three':1, 'four':4}
    swap_unique_keys_values(d)

if __name__ == "__main__":
    main()