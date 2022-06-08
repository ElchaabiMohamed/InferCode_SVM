def compteChiffre(chiffre,nombre):
  cpt=0
  nb=nombre
  while nombre!=0:
    nb=nombre%10
    nombre=nombre//10
    if chiffre==nb:
      cpt=cpt+1
  return cpt