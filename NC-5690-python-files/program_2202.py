def nbChiffres(nombre):
  while nombre!=0:
    nombre=nombre%10
  if nombre==0:
    nombre=1

  return nombre