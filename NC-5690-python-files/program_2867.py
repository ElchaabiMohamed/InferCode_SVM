def compteChiffre(chiffre,nombre):
  res=0
  while nombre!=0:
    if chiffre==nombre//10:
      res+=1
    nombre-=nombre//10
  return res