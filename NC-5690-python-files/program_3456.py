def compteChiffre(chiffre,nombre):
  res=[]
  cpt=0
  if nombre==0:
    res.append(0)
  while nombre!=0:
    res.append(nombre%10)
    nombre=nombre//10
  for i in range(len(res)):
    if res[i]==chiffre:
      cpt=cpt+1
  return cpt