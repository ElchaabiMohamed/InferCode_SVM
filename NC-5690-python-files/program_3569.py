def minimum(liste):
    if len(liste)==0:
      min=None
    else:
      min=liste[0]
      for i in range(1,len(liste)):
        if liste[i]<min:
          min=liste[i]
    return min