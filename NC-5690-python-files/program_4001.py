def distribution(liste,n):
  res=liste[0]*n+1
  for i in range(len(liste)):
    res=liste[i]+1
  return res