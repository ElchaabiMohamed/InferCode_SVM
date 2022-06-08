def maximum(liste):
  if len(liste)==0:
    return None
  else:
    max=liste[0]
    for elem in liste:
      if elem>max:
        max=elem
  return max