def listeSymetrique(l):
    trouve=True
    i=0
    j=-1
    while i<len(l) and j>=-len(l) and trouve!=False:
      if l[i]!=l[j]:
        trouve=False
      i=i+1
      j=j-1
    return trouve
  
l=[1,2,3,1]
 