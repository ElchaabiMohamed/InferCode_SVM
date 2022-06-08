def doubleLettre(mot):
  prec=' '
  for c in mot:
    if prec==c:
      res=True
    else:
      res=False
    prec=c
  return res