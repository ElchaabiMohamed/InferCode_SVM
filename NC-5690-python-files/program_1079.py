def meilleurScoreJoueur(scores,joueurs,nom):
  i=0
  res=0
  while i<len(joueurs):
    if nom==joueurs[i]:
      if res<scores[i]:
        res=scores[i]
    i+=1
  return res