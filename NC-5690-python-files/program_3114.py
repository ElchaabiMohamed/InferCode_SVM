def meilleurScoreJoueur(scores,joueurs,nom):
  res=0
  for i in range (len(joueurs)):
    if nom==joueurs[i]:
      if scores[i]>res:
        res=scores[i]
  return res