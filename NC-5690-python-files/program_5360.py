def doubleChiffre(nombre):
  res=False
  com=[]
  while nombre!=0:
    com.append(nombre%10)
    nombre=nombre//10
    if com in nombre:
      res=True
  return res