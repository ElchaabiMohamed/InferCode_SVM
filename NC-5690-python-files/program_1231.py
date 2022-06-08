def stockerChiffres(nombre):
  i=0
  res=[]
  if nombre==0:
    res=[0]
  while nombre!=0:
    n=nombre//10
    res.append(n%10)
    i+=1
  return res