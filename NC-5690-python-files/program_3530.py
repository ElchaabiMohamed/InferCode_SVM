def doubleLettre(mot):
  res=False
  l1=''
  for l2 in mot:
    if l1==l2:
      res=True
    l1=l2
  
  return res