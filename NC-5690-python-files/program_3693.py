def stockerChiffres(nombre):
  res=[]
  while nombre!=0:
    res.append(nombre%10)
    nombre=nombre//10
  if nombre==0:
    res=0
  return res