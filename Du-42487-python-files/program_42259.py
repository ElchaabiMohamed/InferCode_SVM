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
    newlist = ['antelope']
    nlist = append2list(newlist, list2)
    print(nlist)

    list3 = ['fox', 'chicken']
    nlist = append2list(list3)
    print(nlist)
heh = ['cat']
huh = ['dog']
print((append2list(heh, huh)))
if __name__ == '__main__':
    main()