def meilleurClassementJoueur(scores,joueurs,nom):
  cpt = 0
  while cpt<len(joueurs):
    if joueurs[cpt]==nom:
      return cpt
    cpt+=1
  return -1