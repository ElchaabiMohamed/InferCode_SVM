import sys

# Append l1 to l2. If l2 not supplied default to empty list.
def append2list(l1, l2):
    for i in l1:
        l2.append(i)
    return l2

def main():    

    nlist = append2list(["cat"], ["dog"])
    # nlist should be ['cat', 'dog']
    print(nlist)


    nlist = append2list(["lion"], ['antelope'])
    # nlist should be ['antelope', 'lion']
    print(nlist)


    nlist = append2list(["fox"], ["chicken"])
    # nlist should be ['fox', 'chicken']
    print(nlist)

if __name__ == '__main__':
    main()