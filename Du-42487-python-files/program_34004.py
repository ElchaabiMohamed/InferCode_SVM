def maximum(l):
    if len(l) == 1:
        return l[0]
    elif l[0] > l[1]:
        l.remove(l[1])
    else:
        l.remove(l[0])
    return maximum(l)

def main():
    max = None
    print((maximum([6,5,1,3,4])))
    print((maximum([6,5,11,3,4])))
    print((maximum([6,15,11,13,14])))
    print((maximum([6,15,11,13,4])))

if __name__ == '__main__':
    main()