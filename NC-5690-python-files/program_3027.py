def doubleChiffre(nombre):
  res=False
  prec=0
  while nombre!=0 and not res:
    prec=nombre%10
    nombre=nombre//10
    if nombre==prec:
      res=True
  return res