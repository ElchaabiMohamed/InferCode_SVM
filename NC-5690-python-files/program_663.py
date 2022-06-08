def compteChiffre(chiffre,nombre):
  cpt=0
  i=0
  for i in range(len(nombre)):
    if chiffre==nombre[i]:
      cpt=cpt+1
    i=i+1
  return cpt