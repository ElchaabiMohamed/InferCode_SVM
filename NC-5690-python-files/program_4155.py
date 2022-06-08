def compteChiffre(chiffre,nombre):
  cpt=0
  str(nombre)
  for i in range(nombre):
    if chiffre==nombre[i]:
      cpt=cpt+1
  return cpt