def maximum(l, old_max = None):
    try:
        item = l[0]
    except IndexError:
        item = None

    if item is not None:
        new_l = l[1:]
        return maximum(new_l, item if old_max == None or item > old_max else old_max)
    else:
        return old_max


def main():
    max = None
    print((maximum([6,5,1,3,4])))
    print((maximum([6,5,11,3,4])))
    print((maximum([6,15,11,13,14])))
    print((maximum([6,15,11,13,4])))

if __name__ == '__main__':
    main()