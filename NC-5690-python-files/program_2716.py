def moyenne(liste):
  if liste==():
    res=none
  else:
    x=0
    for i in range(len(liste)):
      x=x+liste[i]
      res=x/len(liste)
  return res