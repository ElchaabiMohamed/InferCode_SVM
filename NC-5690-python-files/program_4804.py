def ecart(liste):
  if liste==[]:
    res=None
  else:
    max0=liste[0]
    min0=liste[0]
    for i in range(1,len(liste)):
      if max0<liste[i]:
        max0=lite[i]
      if min0>liste[i]:
        min0=liste[i]
    res=max0-min0
  return res