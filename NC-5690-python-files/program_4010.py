def compteChiffre(chiffre,nombre):
    cpt=0
    reste=nombre%10
    while reste!=1:
      reste=reste%10
      if reste==chiffre:
        cpt+=1
    if cpt==0:
      cpt=1
    return cpt
    