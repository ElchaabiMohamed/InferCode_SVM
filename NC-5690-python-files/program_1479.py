def listeSymetrique(l):
  i=0
  while i<len(l):
    if l[i]!=l[-(1+i)]:
      return False
  return True