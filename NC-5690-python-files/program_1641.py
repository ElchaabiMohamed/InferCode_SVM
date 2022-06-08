def maximum(liste):
  res=0
  for i in range(len(liste)):
    res=liste[i]
    if res<i:
      res=i
    
      
    return res