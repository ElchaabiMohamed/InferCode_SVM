def minimum(liste):
  if liste == []:
    return None
  else:
    minimum = liste[0]
    for i in range(1,len(liste)):
      if minimum > liste[i]:
        minimum = liste[i]
    return minimum