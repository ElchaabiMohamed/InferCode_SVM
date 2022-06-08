def maximum(liste):
  maxi=liste[0]
  for i in range(len(liste)):
    if liste[i]>maxi:
      maxi=liste[i]
  return maxi