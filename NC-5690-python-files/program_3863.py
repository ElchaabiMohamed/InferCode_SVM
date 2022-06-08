def compteChiffre(chiffre,nombre):
  cpt=0
  for i in nombre:
    if chiffre==nombre[i]:
      cpt=cpt+1
    i=i+1
  return cpt