
def main():
    d ={
    "a":4,
    "b":7,
    "c":10,
    "d":7
    }
    run = swap_keys_values(d)
    print(run)

def swap_keys_values(d):
    d2 ={}
    ds = sorted(list(d.items()), reverse =True)
    for k,v in ds:
        if v not in d2:
            d2[v] = k
    return d2

if __name__ == '__main__':
    main()
