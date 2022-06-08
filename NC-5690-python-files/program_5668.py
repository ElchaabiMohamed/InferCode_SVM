def stockerChiffres(nombre):
  res=[]
  if nombre==0:
    res=[0]
  while nombre!=0:
    res.append(nombre%10)
    nombre//=10
  return res