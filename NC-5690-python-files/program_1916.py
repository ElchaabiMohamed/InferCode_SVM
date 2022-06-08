def meilleurClassementJoueur(scores,joueurs,nom):
  res = - 1
  i = 0
  while i < len(joueurs) and res == -1 :
    if nom == joueurs[i] :
      res = i + 1
    i = i + 1
  return res