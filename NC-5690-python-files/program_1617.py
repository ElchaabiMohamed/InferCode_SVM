def compteChiffre(chiffre,nombre):
  res=[]
  cpt=0
  if nombre==0:
    cpt=1
  while nombre!=0:
    res.append(nombre%10)
    nombre//=10
  for i in range(len(res)):
    if chiffre==res[i]:
      cpt+=1
  return cpt 