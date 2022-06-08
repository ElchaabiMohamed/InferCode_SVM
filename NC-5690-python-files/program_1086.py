def maximum(liste):
    max = -999
    for i in range(0,len(liste)):
      if liste[i] > max:
        max = liste[i]
    return max