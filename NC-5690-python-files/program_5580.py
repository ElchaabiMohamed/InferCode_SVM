def meilleurClassementJoueur(scores,joueurs,nom):
  MS=1
  i=0
  while i<len(joueurs) and nom!=joueurs[i]:
    MS=MS+1
    i=i+1
    if nom not in joueurs:
      MS=-1
  return MS