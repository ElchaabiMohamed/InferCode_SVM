def nbChiffres(nombre):
  res=1
  while nombre!=0:
    nombre=nombre//10
    res=res+1
  return res  