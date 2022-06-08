def doubleChiffre(nombre):
  res=False
  trouve=False
  prec=0
  while nombre!=0 and trouve==False:
    com1=nombre%10
    nombre=nombre//10
    if com1==prec:
      res=True
    prec=com1  
  return res