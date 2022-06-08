def minimum(liste):
  res=100
  for i in range (len(liste)):
    if (liste[i])<res:
      res=(liste[i])
  return res