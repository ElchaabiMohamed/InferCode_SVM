def nbChiffres(nombre):
  res=0
  nb=nombre
  cpt=1
  while nb%10!=0:
    cpt=cpt+1
    nb=nb//10
  return cpt
    
    