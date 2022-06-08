def doubleChiffre(nombre):
  res=False
  com1=0
  while nombre!=0 and not res:
    chiffre=nombre%10
    nombre=nombre//10
    if chiffre==com1:
      res=True
    com1=chiffre
  return res