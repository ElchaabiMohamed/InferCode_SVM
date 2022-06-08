def stockerChiffres(nombre):
  res=[]
  if nombre==0:
    res.append(nombre)
  while nombre!=0:
    res.append(nombre%10)
    nombre=nombre//10
  return res