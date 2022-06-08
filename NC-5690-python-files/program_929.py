def maximum(liste):
    if len(liste)==0:
      res=None
    else:
      res=liste[0]
      for i in range(len(1,liste)):
        if liste[i]>res:
          res=i
    return res