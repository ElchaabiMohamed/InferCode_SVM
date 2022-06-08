def minimum(liste):
  min=liste[0]
  for i in liste: 
    if liste[i]<liste[i+1]:
      min=liste[i]
    else:
      min=None
  return min