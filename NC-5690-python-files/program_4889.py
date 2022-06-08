def compteChiffre(chiffre,nombre):
  cpt=0
  for i in nombre:
    if i==chiffre:
      cpt=cpt+1
    i=i+1
  return cpt