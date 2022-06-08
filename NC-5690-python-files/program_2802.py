def doubleLettre(mot):
  if mot=='':
    res=None
  else:
    prec=''
    res=False
    for lettre in mot:
      if lettre==prec:
        res=True
      prec=lettre
  return res