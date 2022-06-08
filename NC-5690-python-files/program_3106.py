def compteChiffre(chiffre,nombre):
    cpt=0
    decomp=nombre%10
    while decomp!=1:
      if chiffre in decomp:
        cpt+=1
    return cpt