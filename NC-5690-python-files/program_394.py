def doubleChiffre(nombre):
  trouve=False
  prec=None
  while nombre!=0 and not trouve:
    if prec==nombre%10:
      trouve=True
    prec=nombre%10
    nombre//=10
  return trouve