def listeSymetrique(l):
  l2 = l[int(len(l)/2):]
  l2.reverse()
  l = l[:int(len(l)/2)+1]
  res = False
  if l == l2:
    res = True
  
  return res