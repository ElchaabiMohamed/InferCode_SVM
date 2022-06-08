def stockerChiffres(nombre):
  res=[]
  if nombre==0:
    res.append(nombre)
  while nombre!=0:
    res.append(nombre%10)
    n=n//10
  return res