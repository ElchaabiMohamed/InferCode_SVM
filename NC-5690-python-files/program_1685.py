def doubleChiffre(nombre):
  res=False
  compare=nombre%10
  while nombre!=0 and res==False:
    nombre=nombre//10
    if nombre%10==compare:
      res=True
  return res