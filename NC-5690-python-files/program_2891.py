def doubleChiffre(nombre):
  trouve=False
  chPrec=None
  while nombre!=0:
    chiffre=nombre%10
    if chPrec==nombre:
      trouve=True
    nombre=nombre//10
    chPrec=chiffre
  return trouve