def meilleurClassementJoueur(scores,joueurs,nom):
  i=0
  while i<len(joueurs):
    if nom==joueurs[i]:
      return i+1
    i=i+1
  return -1