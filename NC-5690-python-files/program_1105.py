def compteChiffre(chiffre,nombre):
    cpt=0
    i=0
    while i<len(nombre):
      if nombre[i]==chiffre:
        cpt+=1
      i+=1
    return cpt