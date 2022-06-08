def doubleChiffre(nombre):
  res=False
  com=0
  while nombre!=0:
    com=nombre%10
    nombre=nombre//10
    if com in nombre:
      res=True
  return res