def meilleurClassementJoueur(scores,joueurs,nom):
  if nom not in joueurs:
    return -1
  else:
    for i in range(len(joueurs)):
      if joueurs[i]==nom:
        return i+1
   