def meilleurScoreJoueur(scores,joueurs,nom):
  cpt = 0
  while cpt<len(joueurs):
    if joueurs[cpt]==nom:
      return scores[cpt]
    cpt+=1
  return 0