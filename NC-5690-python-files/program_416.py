def compteChiffre(chiffre,nombre):
  if nombre==0:
    res=[0]
  else:
    res=[]
    while nombre!=0:
      res.append(nombre%10)
      nombre//=10
  cpt=0
  for i in range(len(res)):
    if chiffre==res[i]:
      cpt=cpt+1
  return cpt