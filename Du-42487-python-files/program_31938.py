# Append l1 to l2. If l2 not supplied default to empty list.
def append2list(l1, l2=[]):
    for i in l1:
        l2.append(i)
    return l2

def main():    
    list1 = ['cat', 'dog']
    nlist = append2list(list1)
    # nlist should be ['cat', 'dog']
    print(nlist)

    list2 = ['lion']
    nlist = append2list(list2, ['antelope'])
    # nlist should be ['antelope', 'lion']
    print(nlist)

    list3 = ['fox', 'chicken']
    mlist = append2list(list3, [])
    # nlist should be ['fox', 'chicken']
    print(mlist)

if __name__ == '__main__':
    main()
