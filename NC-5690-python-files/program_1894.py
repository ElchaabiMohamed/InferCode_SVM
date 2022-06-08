def compteChiffre(chiffre,nombre):
  cpt=0
  res=[]
  while nombre!=0:
    res.append(nombre%10)
    nombre=nombre//10
  if res==[]:
    res.append(0)
  for i in res:
    if i==chiffre:
      cpt+=1
  return cpt