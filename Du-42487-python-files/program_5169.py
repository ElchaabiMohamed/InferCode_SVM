def append2list(l1, l2=None):
    for i in l1:
        l2.append(i)
    return l2

def main():    
    list1 = ['dog']
    nlist = append2list(list1, ['cat'])
    # nlist should be ['cat', 'dog']
    print(nlist)

    list1 = ['lion']
    nlist = append2list(list1, ['antelope'])
    # nlist should be ['antelope', 'lion']
    print(nlist)

    list1 = ['chicken']
    nlist = append2list(list1, ['fox'])
    # nlist should be ['fox', 'chicken']
    print(nlist)

if __name__ == '__main__':
    main()
