def plusLongueSuite(liste):
  res=0
  for n1 in range(len(liste)):
     for n2 in range (1,len(liste)):
      if n1==n2:
        res=res+1
  
  return res