def ecart(liste):
  if len(liste) == 0 :
  	res = None
  else :
    maxi = liste[0]
    mini = liste[0]
    for i in range (1,len(liste)):
      if liste[i] > maxi : 
        maxi = liste[i]
      elif mini[i] < mini :
        mini = liste[i]
    res = maxi - mini
  return res