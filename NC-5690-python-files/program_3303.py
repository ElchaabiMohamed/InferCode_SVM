def nbOccurrencesJoueur(joueurs,nom):
  i=0
  res=0
  for i in range(len(joueurs)):
    if nom==joueurs[i]:
      res=res+1
    if nom not in joueurs:
      res=0
  return res