def listeSymetrique(l):
  res = True
  i = 0
  while i < len(l)/2 and res == True :
    if l[i] != l[len(l)-i-1] :
      res = False
    i = i + 1
  return res