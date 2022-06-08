def meilleurScoreJoueur(scores,joueurs,nom):
  i=0
  max=0
  while i<len(scores)-1 and i<len(joueurs) and max:
    if nom==joueurs[i] and scores[i]>scores[i+1]:
      max=i
  return max