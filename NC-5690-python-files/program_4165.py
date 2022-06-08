def doubleChiffre(nombre):
  trouve=False
  chPrec=None
  while nombre!=0 and not trouve:
    chiffre=nombre%10
    nombre=nombre//10
    if chPrec==nombre:
      trouve=True
    chPrec=chiffre
  return trouve