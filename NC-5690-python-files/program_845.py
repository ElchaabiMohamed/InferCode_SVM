def maximum(liste):
    max = liste[0]
    for i in range(0,len(liste)):
      if liste[i] > max:
        max = liste[i]
    if len(liste) == 0:
      max = None
    return max