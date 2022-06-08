def meilleurClassementJoueur(scores,joueurs,nom):
  i=0
  while i<len(scores):
    if nom==joueurs[i]:
      return i
    i=i+1
    