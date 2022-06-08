def compteChiffre(chiffre,nombre):
  res=False
  prec=None
  while nombre!=0 and not res:
    nombre=nombre//10
    if chiffre==prec:
      res=True
    prec=chiffre
  return res