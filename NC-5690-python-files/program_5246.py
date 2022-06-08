def maximum(liste):
  res=liste[0]
  for i in liste:
     if res<i:
      return i
  else:
    return res