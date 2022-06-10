import sys

def swap_keys_values(dic):
    return {v:k for (k,v) in list(dic.items())}

def main():
    dic = {"a":4, "b":7, "c":10}
    print((swap_keys_values(dic)))


if __name__ == '__main__':
    main()
