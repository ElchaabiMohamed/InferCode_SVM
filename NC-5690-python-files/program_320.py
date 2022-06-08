def moyenne(liste):
  if len(liste)==0:
    res=None
  else:
    res=0
    for i in range(len(liste)):
      res+=liste[i]
    res=res/len(liste)
  return res