def maximum(liste):
  if len(liste)!=0:
    max=liste[0]
    for elem in liste:
      if elem>max:
        max=elem
    return max