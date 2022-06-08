def moyenne(liste):
  if liste==():
    res=none
  else:
    for i in range (len(liste)):
      x=res+liste[i]
      res=x/len(liste)
  return res