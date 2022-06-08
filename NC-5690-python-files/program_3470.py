def compteChiffre(chiffre,nombre):
  cpt=0
  for i in range(len(nombre)):
    if chiffre==nombre:
      cpt=cpt+1
  return cpt