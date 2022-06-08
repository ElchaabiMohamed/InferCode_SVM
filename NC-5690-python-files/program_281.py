def compteChiffre(chiffre,nombre):
  res=1
  while nombre!=0:
    nombre=nombre//10
    if nombre%10==chiffre:
      res+=1
  return res