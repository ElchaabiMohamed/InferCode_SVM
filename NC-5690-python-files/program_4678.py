def nbOccurrencesJoueur(joueurs,nom):
  res = 0
  i = 0
  while i < len(joueurs) :
    if nom == joueurs[i]:
      res = res + 1
    i = i + 1
  return res 