def compteChiffre(chiffre,nombre):
  cpt=0
  for elem in nombre:
    if elem==chiffre:
      cpt+=1
  return cpt

