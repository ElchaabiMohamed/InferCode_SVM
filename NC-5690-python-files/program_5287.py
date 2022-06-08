def compteChiffre(chiffre,nombre):
    res=0
    nb=nombre
    while nb//10!=0:
      if nb%10==chiffre:
        res=res+1
      nb=nb//10
    if nombre==0 and chiffre==0:
      res=1
      return res
      
      