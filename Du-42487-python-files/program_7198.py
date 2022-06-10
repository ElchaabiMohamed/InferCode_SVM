



def append2list(l1,l2=[]):
    for i in l1:
        l2.append(i)
    return l2


def main():
    list1 = ['cat','dog']
    nlist = append2list(list1)
    print(nlist)

    list2 = ['antelope','lion']
    nlist = append2list(list2)
    print(nlist)

    list3 = ['fox','chicken']
    nlist = append2list(list3)
    print(nlist)


if __name__ == '__main__':
    main()



















































