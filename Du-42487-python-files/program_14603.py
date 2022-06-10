import sys

def swap_unique_keys_values(d):
    d1 = {}
    items = list(d.items())
    for item in items:
        if item[1] not in d1:
            d1[item[1]] = item[0]
        else:
            d1.pop(item[1])
    return d1

def main():
    d = {'a' : 4, 'b' : 7, 'c' : 10, 'd' : 7}
    print((swap_unique_keys_values(d)))

if __name__ == '__main__':
    main()
