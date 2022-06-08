def compteChiffre(chiffre,nombre):
  res=0
  while nombre!=0:
    if nombre//10==chiffre:
      nombre=nombre//10
      res+=1
  return res