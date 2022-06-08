def doubleChiffre(nombre):
  res=False
  prec=None
  while nombre!=0 and not res:
    chiffre=nombre%10
    nombre=nombre//10
    if chiffre==prec:
      res=True
    prec=chiffre
  return trouve