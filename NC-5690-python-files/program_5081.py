def stockerChiffres(nombre):
  cpt=0
  res=[]
  nb=nombre
  while nb!=0:
    res=res+nb%10
    nb=nb//10
  return res
    