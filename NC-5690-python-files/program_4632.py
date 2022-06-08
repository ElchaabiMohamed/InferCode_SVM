def stockerChiffres(nombres):
  res=[]
  while nombres!=0:
    res.append(nombres%10)
    nombres=nombres//10
  return res