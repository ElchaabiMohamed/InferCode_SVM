def ecart(liste):
  if len(liste)==0:
    res=None
  if len(liste)==1:
    res=0
  else:
      max=liste[0] 
      min=liste[0] 
      for i in range (len(liste)):
        if max<liste[i]:
          max=liste[i]
        elif min>liste[i]:
          min=liste[i]
      res=max-min
  return res