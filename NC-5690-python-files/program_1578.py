def maximum(liste):
    res=liste[0]
    for i in range (len(liste)):
      if liste[i]>res :
        res=liste[i]
    return res