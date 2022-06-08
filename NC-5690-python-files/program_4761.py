def stockerChiffres(nombre):
  res=[]
  cpt=0
  while nombre!=0:
    res.append(nombre%10)
    nombre=nombre//10
    cpt+=1
  if cpt==0:
    res.append(0)
  return res