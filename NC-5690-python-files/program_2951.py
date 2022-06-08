def compteChiffre(chiffre,nombre):
    cpt=0
    decomp=nombre%10
    while decomp!=1:
      decomp=decomp%10
      if decomp==chiffre:
        cpt+=1
    if cpt==0:
      cpt=1
    return cpt
    