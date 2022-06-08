def compteChiffre(chiffre,nombre):
    cpt=0
    decomp=nombre
    x=nombre%10
    while decomp!=0:
      x=nombre%10
      if x!=chiffre:
        decomp=decomp//10
        x=decomp%10
      else:
        cpt+=1
    return cpt