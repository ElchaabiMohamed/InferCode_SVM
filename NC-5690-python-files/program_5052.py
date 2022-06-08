def nbOccurrencesJoueur(joueurs,nom):
  res=0
  for i in joueurs:
    if nom==i:
    	res=res+1
  return res