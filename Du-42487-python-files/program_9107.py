def reverse_list(l, l1=None):
    if l1 is None: l1 = []
    if l == []: return l1
    l1.append(l[-1])
    return reverse_list(l[:-1], l1)

def main():
    print((reverse_list([1,2,3])))
    print((reverse_list([3,4,5,6])))
    print((reverse_list([1,2])))

if __name__ == '__main__':
    main()