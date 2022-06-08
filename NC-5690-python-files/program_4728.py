def doubleChiffre(nombre):
  res=False
  prec=nombre%10
  while nombre!=0 and res==False:
    nombre=nombre//10
    if nombre%10==prec:
      res=True
    prec=nombre%10
  return res