def compteChiffre(chiffre,nombre):
  cpt=0
  res=[]
  if nombre==0:
    cpt=1
  while nombre!=0:
    res.append(nombre%10)
    nombre=nombre//10
  for i in range (len(res)):
    if res[i]==chiffre:
      cpt+=1
  return cpt
  