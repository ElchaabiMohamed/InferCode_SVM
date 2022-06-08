def compteChiffre(chiffre,nombre):
  cpt=0
  for i in range(len(nombre)):
    if nombre[i]==chiffre:
      cpt+=1
  return cpt

