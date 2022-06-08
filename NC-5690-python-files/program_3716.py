def meilleurScoreJoueur(scores,joueurs,nom):
  trouve=False
  i=0
  res=0
  while i<len(score) and not trouve:
    if nom==joueur[i]:
      trouve=True
      res=score[i]
    i=i+1
  return res