def maximum(liste):
  if len(liste)==0:
    res=None
  else:
    res=liste[0]
    for elem in liste:
      if res<elem:
        res=elem
  return res