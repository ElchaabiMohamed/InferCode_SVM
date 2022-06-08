def meilleurScoreJoueur(scores,joueurs,nom):
  i=0
  while i<len(joueurs):
    if nom==joueurs[i]:
      return scores[i]
    i=i+1
  return 0