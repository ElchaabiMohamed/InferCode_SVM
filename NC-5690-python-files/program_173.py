def ecart(liste):
  if len(liste)==0:
    res=None
  else:
    res=0
    maxi=liste[0]
    mini=liste[0]
    for i in range(len(liste)):
      if liste[i]>maxi:
        maxi=liste[i]
    for i in range(len(liste)):
      if liste[i]<mini:
        mini=liste[i]
    res=maxi-mini
  return res