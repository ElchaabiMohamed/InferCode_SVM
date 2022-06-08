def compteChiffre(chiffre,nombre):
    cpt=0
    x=nombre%10
    decomp=nombre
    while decomp!=0:
      if x==chiffre:
        cpt+=1
        decomp=decomp//10
        x=decomp%10
      else:
        decomp=decomp%10
        x=decomp//10
    if cpt==0:
      cpt=1
    return cpt