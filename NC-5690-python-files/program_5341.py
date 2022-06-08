def meilleurClassementJoueur(scores,joueurs,nom):
  res=0
  if nom not in joueurs:
    res=-1
  else:
    for i in range(len(joueurs)):
      if joueurs[i]==nom:
        res=i
  return res   