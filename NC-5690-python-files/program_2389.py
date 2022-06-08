def stockerChiffres(nombre):
  res=[]
  while nombre!=0:
    res.append(nombre%10)
    nombre=nombre//10
  if res==0:
    res.append(0)
  return res