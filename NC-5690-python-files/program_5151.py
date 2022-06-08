def meilleurScoreJoueur(scores,joueurs,nom):
  trouve=False
  i=0
  res=0
  while i<len(scores) and not trouve:
    if nom==joueurs[i]:
      trouve=True
      res=scores[i]
    i=i+1
  return res