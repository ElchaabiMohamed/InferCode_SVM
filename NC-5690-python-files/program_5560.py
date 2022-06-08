def meilleurScoreJoueur(scores,joueurs,nom):
  MS=0
  i=0
  while i<len(joueurs) and MS==0:
    if nom==joueurs[i]:
      MS=scores[i]
    i=i+1
    if nom not in joueurs:
      MS=0
  return MS
