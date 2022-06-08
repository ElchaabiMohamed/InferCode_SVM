def minimum(liste):
  if len(liste)!=0:
    min=liste[0]
    for elem in liste:
      if elem<min:
        min=elem
    return min