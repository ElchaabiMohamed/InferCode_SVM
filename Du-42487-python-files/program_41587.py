def minimum(l):
    if len(l) == 1:
        return l[0]
    else:
        min_ret = minimum(l[1:])
        return l[0] if l[0] < min_ret else min_ret

def main():
    min = None
    print((minimum([6,5,1,3,4])))
    print((minimum([6,5,11,3,4])))
    print((minimum([6,15,11,13,14])))
    print((minimum([6,15,11,13,4])))

if __name__ == '__main__':
    main()
