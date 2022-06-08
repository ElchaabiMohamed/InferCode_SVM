def compteChiffre(chiffre,nombre):
    cpt=0
    decomp=nombre%10
    while decomp!=1:
      decomp=nombre%10
      if decomp==chiffre:
        cpt+=1
        decomp=decomp%10
    return cpt
  