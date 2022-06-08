def compteChiffre(chiffre,nombre):
    cpt=0
    for val in nombre:
      if val==chiffre:
        cpt+=1
    return cpt
  