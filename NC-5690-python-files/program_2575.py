def doubleLettre(mot):
  res=0
  l1=''
  for l2 in mot:
    if l1==l2:
      res=res+1
    l1=l2
  
  return res