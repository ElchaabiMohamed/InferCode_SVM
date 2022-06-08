def ecacrt(liste):
  if len(liste)==0:
    return None
  else:
    max = liste[0]
    min = liste[0]
    for i in range(1,len(liste)):
      if liste[i]>max:
        max = liste[i]
      elif liste[i]<min:
        min = liste[i]   
  return (max-min)