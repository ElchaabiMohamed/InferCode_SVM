def meilleurScoreJoueur(score,joueur,nom):
  for i in range(len(joueur)):
     if joueur[i]==nom:
      return score[i]
  return 0