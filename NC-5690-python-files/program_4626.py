def listeSymetrique(l):
  l2 = l[int(len(l)/2):]
  l2.reverse()
  l = l[:int(len(l)/2)+1]
  res = True
  if l != l2:
    res = False
  
  return res