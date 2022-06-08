def compteChiffre(chiffre,nombre):
    res=False 
    cpt=0
    prec=None
    while nombre!=0 and not res:
      nb=nombre%10
      nombre=nombre//10
      if chiffre==prec:
        cpt=cpt+1
      prec=nb
    if chiffre==0 and nombre==0:
      cpt=1
    return cpt
    