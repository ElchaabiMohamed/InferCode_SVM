def stockerChiffres(nombre):
  i=0
  res=[]
  if nombre==0:
    res=[0]
  while nombre!=0:
    nombre=nombre//10
    res=res.append(nombre)
    i+=1
  return res