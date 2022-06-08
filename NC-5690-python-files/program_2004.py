def meilleurClassementJoueur(scores,joueurs,nom):
  if nom not in joueurs:
    res=-1
  else:
    for i in range(len(joueurs)):
      if joueurs[i]==nom:
        return i
  return res