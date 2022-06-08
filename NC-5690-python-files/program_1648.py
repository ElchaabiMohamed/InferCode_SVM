def meilleurClassementJoueur(scores,joueurs,nom):
  c=True
  if nom in joueurs:
    while i<len(joueurs) and c:
      if nom==joueurs[i]:
        res=i+1
  else:
    res=-1
  return res
