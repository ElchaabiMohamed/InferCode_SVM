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
    nlist = append2list(['antelope'], list2)
    # nlist should be ['lion', 'antelope']
    print(nlist)

    list3 = ['fox', 'chicken']
    nlist = append2list(list3)
    alist = list(set(nlist) - set(list1) - set(list2))
    # nlist should be ['fox', 'chicken']
    print(alist)

if __name__ == '__main__':
    main()
