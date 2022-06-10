# Append l1 to l2. If l2 not supplied default to empty list.
def append2list(l1,l2=[]):
    for i in l1:
        l2.append(i)
    return l2

def main():    
    nlist = ['cat', 'dog']

    print(nlist)

    nlist = ['lion', 'antelope']

    print(nlist)

    nlist= ['fox', 'chicken']

    print(nlist)

if __name__ == '__main__':
    main()
