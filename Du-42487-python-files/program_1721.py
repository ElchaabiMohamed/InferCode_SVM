def append2list(l1, l2 = None):
  if l2 == None:
    l2 = []
  for i in l1:
    l2.append(i)
  return l2
    
def main():    
    list1 = ['dog']
    nlist = append2list(list1, ['cat'])
    print(nlist)

    list2 = ['lion']
    nlist = append2list(list2, ['antelope'])
    print(nlist)

    list3 = ['chicken']
    nlist = append2list(list3, ['fox'])
    print(nlist)

if __name__ == '__main__':
    main()








