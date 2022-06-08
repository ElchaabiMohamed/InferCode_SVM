def compteChiffre(chiffre,nombre):
    cpt=0
    decomp=nombre
    while decomp!=0:
      if decomp==chiffre:
        cpt+=1
        decomp=decomp%10
    if cpt==0:
      cpt=1
    return cpt
    