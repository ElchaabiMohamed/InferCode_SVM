#!usr/bin/env python3

def power(n, m):
    return 1 if not m else n * power(n, m - 1)

def main():
    print((power(2,3)))
    print((power(4,4)))
    print((power(2,32)))
    print((power(10,3)))
    print((power(8,0)))

if __name__ == '__main__':
    main()