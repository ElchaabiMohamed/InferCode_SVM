def listeSymetrique(liste):
  res = True
  i = 0
  while i<(len(liste)//2):
    if liste[i] != liste[len(liste)-1-i] :
      res = False
    i = i + 1
  return res