def meilleurScoreJoueur(score,joueur,nom):
  i=0
  while i<len(score):
    if nom==joueur[i]:
      return score[i]
    i+=1
  return 0