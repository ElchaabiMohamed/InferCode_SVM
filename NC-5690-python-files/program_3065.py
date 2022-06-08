def meilleurClassementJoueur(scores,joueurs,nom):
  c=True
  i=0
  if nom in joueurs:
    while i< len(joueurs) and c:
      if nom==joueurs[i]:
        res=i+1
        c=False
      i+=1
  else:
    res=-1
  return res
