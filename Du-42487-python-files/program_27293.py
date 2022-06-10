from math import inf

def minimum(l):
    min = inf

    for item in l:
        min = item if item < min else min

    return min


def main():
    min = None
    print((minimum([6,5,1,3,4])))
    print((minimum([6,5,11,3,4])))
    print((minimum([6,15,11,13,14])))
    print((minimum([6,15,11,13,4])))

if __name__ == '__main__':
    main()