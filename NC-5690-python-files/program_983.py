def compteChiffre(chiffre,nombre):
    res=0
    nb=nombre
    while nb//10!=0:
      if nb%10==chiffre:
        res=res+1
      nb=nb//10
      
      