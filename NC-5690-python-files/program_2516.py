def plusLongueSuite(liste):
  res=0
  n1=liste[0]
  for n2 in range (1,len(liste)):
    if n1==n2:
      res=res+1
    n1=n2
  
  return res