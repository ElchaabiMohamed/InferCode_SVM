def plusLongueSuite(liste):
  res=0
  for n1 in range(0,len(liste)):
    
     for n2 in range (2,len(liste)):
      if n1==n2:
        res=res+1
  
  return res