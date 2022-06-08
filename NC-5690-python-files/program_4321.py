def compteChiffre(chiffre,nombre):
    res=0
    for i in nombre:
      if i==chiffre:
        res=res+1
    return res