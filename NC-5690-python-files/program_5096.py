def doubleChiffre(nombre):
  trouve=False
  prec=None
  while nombre!=0 and not trouve:
    if prec==nombre%10:
      trouve=True
    nombre=nombre//10
    prec=nombre%10
  return trouve