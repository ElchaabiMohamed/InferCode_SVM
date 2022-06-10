def minimum(a):
    if len(a) == 1:
        return a[0]

    smallest = a.pop(0)
    x = minimum(a)
    if smallest > minimum(a):
        smallest = x

    return smallest

def main():
    min = None
    print((minimum([6,5,1,3,4])))
    print((minimum([6,5,11,3,4])))
    print((minimum([6,15,11,13,14])))
    print((minimum([6,15,11,13,4])))

if __name__ == '__main__':
    main()

