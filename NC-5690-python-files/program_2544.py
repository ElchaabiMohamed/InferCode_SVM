def compteChiffre(chiffre,nombre):
  cpt=0
  while nombre!=0:
    nombre=nombre//10
  if nombre==chiffre:
    cpt=cpt+1
  return cpt