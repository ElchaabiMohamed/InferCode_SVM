def compteChiffre(chiffre,nombre):
    cpt=0
    decomp=nombre//10
    while decomp!=0:
      if chiffre in decomp:
        cpt+=1
    return cpt
  