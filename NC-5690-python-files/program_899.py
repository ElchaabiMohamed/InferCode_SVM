def minimum(liste):
  if liste==():
    res=None
  else:
      res=liste[0]
      for i in range(len(liste)):
        if res>liste[i]:
          res=liste[i]
  return res