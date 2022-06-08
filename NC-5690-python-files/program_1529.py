def suiteAri(liste):
  res = True
  raison = liste[1]-liste[0]
  while res and i < len(liste)-1 :
    if liste[i]+raison != liste[i+1]:
      res = False
  return res