def maximum(a):
    if len(a) == 1:
        return a[0]

    biggest = a.pop()
    x = maximum(a)
    if biggest < x:
        biggest = x

    return biggest

def main():
    min = None
    print((maximum([6,5,1,3,4])))
    print((maximum([6,5,11,3,4])))
    print((maximum([6,15,11,13,14])))
    print((maximum([6,15,11,13,4])))

if __name__ == '__main__':
    main()

