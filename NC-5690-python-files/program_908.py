def ecart(liste):
  if len(liste)==0:
    return None
  max=liste[0]
  for i in range (1,len(liste)):
    if liste[i]>max:
        max=liste[i]
  min=liste[0]
  for i in range(1,len(liste)):
    if liste[i]<min:
        min=liste[i]
    ecart=max-min
  return ecart
  
    