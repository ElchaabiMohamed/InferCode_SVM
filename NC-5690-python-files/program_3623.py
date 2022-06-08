def doubleLettre(mot):
  prec=''
  res=False
  for lettre in mot:
    if lettre==prec:
      res=True
  return res