def listeSymetrique(l):
  l2 = []
  flag = False
  i = 0
  while flag == False and i < len(l)-1:
    if l[i] < l[i+1]:
      l2.append(l[i])
      l2.append(l[i+1])
      i=+2
    else:
      l2.reverse()
      flag = True
  
  print(l[i+1:],l2)
  if l[i+1:] == l2:
    res = True
  else:
    res = False
  
  return res