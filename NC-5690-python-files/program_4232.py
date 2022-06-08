def ecart(liste):
  if len(liste)==0:
    res=None
  elif len(liste)==1:
    res=0
  else:
    res=0
    res1=liste[0]
    res2=liste[0]
    for i in range(len(liste)):
      if res1>liste[i]:
        res1=liste[i]
      if res2<liste[i]:
        res2=liste[i]
    res=res2-res1
  return res