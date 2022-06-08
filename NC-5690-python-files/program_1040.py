def compteChiffre(chiffre,nombre):
    cpt=0
    decomp=nombre%10
    if decomp==chiffre:
      cpt+=1
    return cpt
  