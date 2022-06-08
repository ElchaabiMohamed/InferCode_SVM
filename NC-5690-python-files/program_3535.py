def stockerChiffres(nombre):
  if nombre==0:
    res=[0]
  else:
    res=[]
    while nombre!=0:
      res.append(nombre%10)
      nombre//=10
  return res