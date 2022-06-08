def meilleurClassementJoueur(scores,joueurs,nom):
  i=0
  trouve=False
  res=0
  while i<len(joueurs) and not trouve :
    if nom==joueurs[i] :
      trouve=True
    i+=1
  if trouve==True :
    res=i
  else :
    res=-1
  return res