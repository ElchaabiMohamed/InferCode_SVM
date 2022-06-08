def doubleChiffre(nombre):
  trouve=False
  while nombre!=0:
    x=nombre%10
    nombre=nombre//10
    y=nombre%10
    if x==y:
      trouve=True
  return trouve