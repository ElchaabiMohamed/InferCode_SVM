def meilleurClassementJoueur(scores,joueurs,nom):
  MS=0
  i=0
  while i<len(joueurs) and nom!=joueurs[i]:
    MS=MS+1
    i=i+1
    if nom not in joueurs:
      MS=0
  return MS