def listeSymetrique(l):
  i=0
  res = True
  while res == True and i < len(l)-1:
    i+=1
    if l[i] != l[len(l)-i-1]:
      res = False
  return res

def nombreSymetrique(nombre):
  l = []
  for nb in str(nombre):
    l.append(int(nb))
 
  return listeSymetrique(res)