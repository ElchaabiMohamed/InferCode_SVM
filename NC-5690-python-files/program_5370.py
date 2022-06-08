def doubleLettre(mot):
  res=None
  
  for c in mot:
    if c==c:
      res=True
    else:
      res=False
      
  return res