def moyenne(liste):
  if len(liste)==0:
    res=None
  else:
    num=0
    for i in range(len(liste)):
      num=num+liste[i]
    res=num/len(liste)
  return res