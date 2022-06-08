def maximum(liste):
    res = liste[0]
    for i in range(0,len(liste)):
      if liste[i] > res :
        res = liste[i]
    if len(liste) == 0:
      res = None
    return res