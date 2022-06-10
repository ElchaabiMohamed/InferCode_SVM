# Append l1 to l2. If l2 not supplied default to empty list.
def append2list(l1, l=[]):
    l2 = []
    for item in l1:
        l2.append(item)

    for item in l:
        l2.append(item)

    return l2

def main():    
    list1 = ['cat', 'dog']
    nlist_1 = append2list(list1)
    # nlist should be ['cat', 'dog']
    print(nlist_1)

    list2 = ['lion']
    nlist_2 = append2list(list2, ['antelope'])
    # nlist should be ['antelope', 'lion']
    print(nlist_2)

    list3 = ['fox', 'chicken']
    nlist_3 = append2list(list3)
    # nlist should be ['fox', 'chicken']
    print(nlist_3)

if __name__ == '__main__':
    main()