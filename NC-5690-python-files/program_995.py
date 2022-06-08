def stockerChiffres(nombre):
  res=[]
  if nombre==0:
    res=[0]
  while nombre!=0:
    res.append(n%10)
    nombre=nombre//10
  return res