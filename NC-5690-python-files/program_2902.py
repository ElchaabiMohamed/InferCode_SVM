def doubleChiffre(nombre):
  res=0
  x=nombre%10
  while nombre>=10:
    y=x//10
    if x==y:
      res=True
    else:
      res=False
  return res