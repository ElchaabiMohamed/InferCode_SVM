def doubleChiffre(nombre):
  while nombre!=0:
    temp = nombre%10
    nombre-=nombre%10
    nombre/=10
    if nombre==temp:
      return True
  return False