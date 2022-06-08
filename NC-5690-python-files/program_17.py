def maximum(liste):
  if len(liste)==0:
    res=None
  else:
    maxi=liste[0]
    for i in range(len(liste)):
      if liste[i]>maxi:
        maxi=liste[i]
  return maxi