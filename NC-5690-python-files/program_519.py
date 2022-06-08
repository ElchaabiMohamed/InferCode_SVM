def symetrique(l):
  
  l2 = l[int(len(l)/2):]
  l2.reverse()
  if len(l)%2 == 0:
    l = l[:int(len(l)/2)]
  else:
    l = l[:int(len(l)/2)+1]
  res = True
  print(l,l2)
  if l != l2:
    res = False
  
  return res