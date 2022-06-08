def somme(liste):
  if liste == []:
    return 0
  else:
    res = liste[0]
    for i in range(1,len(liste)):
      res += liste[i]
    return res