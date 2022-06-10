def maximum(l):
    min = None

    for item in l:
        min = item if min == None or item > min else min

    return min


def main():
    min = None
    print((maximum([6,5,1,3,4])))
    print((maximum([6,5,11,3,4])))
    print((maximum([6,15,11,13,14])))
    print((maximum([6,15,11,13,4])))

if __name__ == '__main__':
    main()