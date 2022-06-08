def compteChiffre(chiffre,nombre):
  cpt=0
  if nombre==0:
   cpt=1
  while nombre!=0:
    nombre=nombre//10
  if nombre==chiffre:
    cpt=cpt+1
  return cpt