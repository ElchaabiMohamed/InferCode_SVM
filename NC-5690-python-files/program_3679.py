def compteChiffre(chiffre,nombre):
  res=None
  while nombre!=0:
    if nombre%10==chiffre:
      res=res+1
    nombre=nombre//10
  return res