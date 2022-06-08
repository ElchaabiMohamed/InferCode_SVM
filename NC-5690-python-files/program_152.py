def meilleurScoreJoueur(scores,joueurs,nom):
  res=0
  for i in range(len(joueurs)):
    if joueurs[i]==nom:
      return score[i]
  return res