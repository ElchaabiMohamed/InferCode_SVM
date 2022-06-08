def compteChiffre(chiffre,nombre):
  cpt=0
  if nombre==0 and cpt==0:
    cpt=1
  while nombre>0:
    if nombre%10==chiffre:
      cpt+=1
    nombre=nombre//10
  return cpt