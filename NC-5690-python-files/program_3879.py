def stockerChiffres(nombre):
  res=[]
  while nombre!=0:
    nombre=nombre//10
    res=nombre+res
  if nombre==0:
    res=res+0
  return res