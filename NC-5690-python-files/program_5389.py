def nbChiffres(nombre):
  while nombre//10>0:
    nombre=nombre%10
  if nombre==0:
    nombre=1
  return nombre