def doubleLettre(mot):
  l1=" "
  for l2 in mot:
    if l1==" " and l2!=" ":
      res=True
    else:
      res=False
      l2=l1
  return res