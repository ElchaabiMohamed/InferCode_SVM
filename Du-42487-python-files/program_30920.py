# Append l1 to l2. If l2 not supplied default to empty list.
def append2list(l1, l2=[]):
    newL = list(l2)
    for i in l1:
        newL.append(i)
    return newL

def main():    
    list1 = ['cat', 'dog']
    nlist = append2list(list1)
    print(nlist)

    list2 = ['lion']
    nlist = append2list(list2, ['antelope'])
    print(nlist)

    list3 = ['fox', 'chicken']
    nlist = append2list(list3)
    print(nlist)

if __name__ == '__main__':
    main()
