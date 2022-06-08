def compteChiffre(chiffre,nombre):
  res=[]
  cpt=0
  if nombre==0:
    res.append(nombre)
  while nombre!=0:
    res.append(nombre%10)
    nombre=nombre//10
  for elem in range(len(res)):
    if elem==chiffre:
      cpt=cpt+1
  return cpt