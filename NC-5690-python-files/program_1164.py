def doubleLettre(mot):
  c1=(0,len(mot),2)
  c2=(1,len(mot),2)
  for elem in mot:
    if c1==c2:
      res=True
  else:
    res=False
  return res