def compteChiffre(chiffre,nombre):
  cpt=0
  for i in range(min(len(nombre))):
    if chiffre==nombre:
      cpt=cpt+1
  return cpt