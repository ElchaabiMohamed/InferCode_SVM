def doubleLettre(mot):
  res=None
  prev=" "
  for c in mot:
    if prev==" " and c!=" ":
      res=True
    else:
      res=False
      
  return res