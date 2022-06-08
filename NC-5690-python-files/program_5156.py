def ecart(liste):
  if len(liste)==0:
    res=None
  elif len(liste)==1:
    res=0
  else:
    res=0
    res1=liste[0]
    res2=liste[0]
    for i in range(1,len(liste)):
      if res<liste[i]:
        res1=liste[i]
      elif res>liste[i]:
        res2=liste[i]
    res=res1-res2
  return res