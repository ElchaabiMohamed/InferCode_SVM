def compteChiffre(chiffre,nombre):
  cpt=0
  res=False
  prec=None
  while nombre!=0 and not res:
    nombre=nombre//10
    if chiffre==prec:
      res=True
    prec=chiffre
    cpt=cpt+1
  return cpt
