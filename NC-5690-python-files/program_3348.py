def compteChiffre(chiffre,nombre):
    cpt=0
    reste=nombre%10
    while reste!=0:
      reste=reste%10
      if reste==chiffre:
        cpt+=1
    return cpt
    