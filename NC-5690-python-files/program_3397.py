def stockerChiffres(nombres):
  res=[]
  if nombres==0:
    res=0
  while nombres!=0:
    res.append(nombres%10)
    nombres=nombres//10
  return res