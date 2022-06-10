def swap_unique_keys_values(d):
    values = list(d.values())
    items = [(y,x) for (x,y) in list(d.items())]


    d2 ={v : k for (k,v) in sorted(items)}
    return(d2)




def main():
    d = {'d': 7, 'b': 7, 'a': 4, 'c': 10}
    swap_unique_keys_values(d)

if __name__ == "__main__":
    main()