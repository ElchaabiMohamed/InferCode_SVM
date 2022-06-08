def meilleurClassementJoueur(scores,joueurs,nom):
    if nom not in joueurs:
      return -1
    for i in range(len(joueurs)):
      if nom==joueurs[i]:
        return i+1