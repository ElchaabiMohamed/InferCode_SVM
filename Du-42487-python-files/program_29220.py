# Append l1 to l2. If l2 not supplied default to empty list.
def append2list(l1, l2=[]):
    for i in l1:
        l2.append(i)
    return l2

#adding the contents of the first list to the second list. if the second list is not specified then it is an empty list. 

def main():    
    list1 = ['cat', 'dog']
    nlist = append2list(list1)
    # nlist should be ['cat', 'dog']
    print(nlist)
#list 1 is cat, dog. after the function is used, the new list is going to be cat, dog

    list2 = ['lion']
    nlist = nlist + append2list(list2, ['antelope'])
    # nlist should be ['antelope', 'lion']
    print(nlist)

#list 2 

    list3 = ['fox', 'chicken']
    nlist = nlist + append2list(list3)
    # nlist should be ['fox', 'chicken']
    print(nlist)

if __name__ == '__main__':
    main()



#outputs

#1. cat, dog 
#2. antelope, lion
#3. chicken, fox 
