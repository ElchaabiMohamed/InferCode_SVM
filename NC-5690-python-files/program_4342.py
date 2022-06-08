def compteChiffre(chiffre,nombre):
    cpt=0
    decomp=nombre%10
    while decomp!=1:
      if decomp!=chiffre:
        decomp=decomp%10
      else:
        cpt+=1
    return cpt
  