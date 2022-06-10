def minimum(l, old_min = None):
    try:
        item = l[0]
    except IndexError:
        item = None

    if item is not None:
        new_l = l[1:]
        return minimum(new_l, item if old_min == None or item < old_min else old_min)
    else:
        return old_min


def main():
    min = None
    print((minimum([6,5,1,3,4])))
    print((minimum([6,5,11,3,4])))
    print((minimum([6,15,11,13,14])))
    print((minimum([6,15,11,13,4])))

if __name__ == '__main__':
    main()