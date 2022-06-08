def compteChiffre(chiffre,nombre):
    cpt=0
    for x in nombre:
      if x==chiffre:
        cpt+=1
    return cpt
  