def meilleurScoreJoueur(scores,joueurs,nom):
  res=0
  for i in joueurs:
    if nom==i:
      if scores[i]>res:
        res=scores[i]
  return res