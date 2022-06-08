def ecart(liste):
  if len(liste)==0:
    res=None
  elif len(liste)==1:
    res=0
  else:
    res=0
    m1=liste[i]
    for i in range(len(liste)):
      if m1>liste[i]:
        m1=liste[i]
      if m2<liste[i]:
        m2=liste[i]
    res=m1-m2
  return res