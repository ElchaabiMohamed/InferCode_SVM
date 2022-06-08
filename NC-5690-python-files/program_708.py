def ecart(liste):
  if liste==[]:
    res=None
  else:
    maxi=liste[0]
    mini=liste[0]
    for i in range(1,len(liste)):
      if liste[i]<mini:
        mini=liste[i]
      elif liste[i]>maxi:
        maxi=liste[i]
  return res