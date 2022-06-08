def compteChiffre(chiffre,nombre):
    res=0
    nb=[]
    while nombre!=0:
      nb=nb+nombre%10
      nombre=nombre//10
    for i in range(nb):
      if nb[i]==chiffre:
        res=res+1
    return res