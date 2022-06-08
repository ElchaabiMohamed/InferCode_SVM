def doubleChiffre(nombre):
  trouve=False
  chPrec=None
  while nombre!=0:
    chPrec=nombre//10
  if chPrec==nombre:
    trouve=True
  else:
    trouve=False
  return trouve