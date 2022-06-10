import sys
# Append l1 to l2. If l2 not supplied default to empty list.
def append2list(l1, l2=[]):
    for i in l1:
        l2.append(i)
    return l2

def main():    
    list1 = ['apple', 'banana']
    nlist = append2list(list1)
    # nlist should be ['cat', 'dog']
    print(nlist)

    list2 = ['pineapple']
    nlist = append2list(list2, ['orange'])
    # nlist should be ['lion', 'antelope']
    print(nlist)

    list3 = ['coconut', 'mango']
    nlist = append2list(list3,[])
    # nlist should be ['fox', 'chicken']
    print(nlist)

if __name__ == '__main__':
    main()


