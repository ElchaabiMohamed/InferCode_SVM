def doubleChiffre(nombre):
  res=False
  Prec=None
  while nombre!=0 and not res:
    chiffre=nombre%10
    nombre=nombre//10
    if chiffre==prec:
      res=True
    Prec=chiffre
  return trouve