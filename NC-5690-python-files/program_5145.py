def doubleLettre(mot):
  prec=' '
  for c in mot:
    if prec==' ' and c!=' ':
      prec=c
      if prec==c:
        res=True
  return res