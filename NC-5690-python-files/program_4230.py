def stockerChiffres(nombre):
  res=[]
  chiffre=0
  nb=nombre
  while nb:
    chiffre=nb%10
    nb=nb//10
    res=res+[chiffre]
  if len(res)==0:
    res=[0]
  return res