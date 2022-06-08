def listeSymetrique(l):
    trouve=False
    i=0
    j=-1
    while i<len(l) and j<=-len(l):
      if l(i)==l(j):
        trouve=True
      else:
        trouve=False
      i=i+1
      j=j-1
    return trouve
  
      