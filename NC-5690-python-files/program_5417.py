def doubleLettre(mot):
  c1=(0,len(mot),2)
  c2=(1,len(mot),2)
  for c1 in mot:
    if c1!=c2:
      res=False
    else:
      res=True
  return res