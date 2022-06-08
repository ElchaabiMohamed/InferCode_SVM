def maximum(liste):
  if len(liste)==0:
    res=None
  else:
    for i in liste:
      if res<liste[i]:
        res=liste[i]
  return res