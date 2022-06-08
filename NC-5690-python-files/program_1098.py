def compteChiffre(chiffre,nombre):
  cpt=0
  while nombre!=0:
    if chiffre==nombre%10:
      cpt+=1
    nombre-=nombre//10
  return cpt