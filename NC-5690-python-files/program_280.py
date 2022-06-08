def maximum(liste):
  if liste==():
    res=none
  else:
    res=liste[1]
    for i in range (len(liste)):
      if res<liste[i]:
        res=liste[i]
  return res