def doubleChiffre(Nombre):
  i=0
  prec=False
  while Nombre!=0 and prec==False:
    i=Nombre%10
    Nombre=Nombre//10
    if i==Nombre%10:
      prec=True
  return prec