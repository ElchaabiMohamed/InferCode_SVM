def compteChiffre(chiffre,nombre):
  cpt=0
  res=False
  prec=None
  while nombre!=0 and not res:
    numero=nombre%10
    nombre=nombre//10
    if chiffre==prec:
      cpt=cpt+1
    prec=numero
  if chiffre==0 and nombre==0:
    cpt=1
  return cpt 