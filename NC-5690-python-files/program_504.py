def meilleurScoreJoueur(scores,joueurs,nom):
  trouve=False
  i=0
  res=0
  while i<len(joueurs) and i<len(scores) and trouve==False:
    if nom==joueurs[i]:
      trouve=True
      res=scores[i]
    i=i+1
    if nom!=joueurs[i]:
      res=0
      trouve=True
  return res