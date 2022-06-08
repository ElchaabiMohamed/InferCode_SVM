def stockerChiffres(nombre):
  i=0
  res=[]
  if nombre==0:
    res=[0]
  while nombre!=0:
    res=res+[nombre//10]
    i+=1
  return res