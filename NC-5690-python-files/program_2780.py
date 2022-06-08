def doubleLettre(mot):
  res=False
  
  for c in mot:
    if c==c:
      res=True
      
  return res