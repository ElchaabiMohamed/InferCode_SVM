def compteChiffre(chiffre,nombre):
    cpt=0
    decomp=nombre
    while decomp!=0 and decomp!=chiffre:
      decomp=decomp//10
      cpt+=1
    return cpt