def sommeNbPairs(liste):
  if len(liste)==0:
    res=0
  else:
    res=liste[0]
    for i in range(1,len(liste)):
      if liste[i]%2==0:
        res=res+liste[i]
  return res
      
      
  