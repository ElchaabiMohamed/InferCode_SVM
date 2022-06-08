def doubleLettre(mot):
  l1=" "
  for l2 in mot:
    if l1==" " and l2!=" ":
      res=True
    l2=l1
  else:
    res=False
  return res