import sys

def swap_keys_values(d):
    d1 = {}
    items = list(d.items())
    for item in items:
        d1[item[1]] = item[0]
    return d1

#def main():
#    d = {'a' : 4, 'b' : 7, 'c' : 10}
#    print (swap_keys_values(d))

#if __name__ == '__main__':
#    main()

