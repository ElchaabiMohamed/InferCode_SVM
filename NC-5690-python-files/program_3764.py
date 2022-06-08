def nbOccurrencesJoueur(joueurs,nom):
  res=0
  for i in range(len(joueurs)):
    if joueurs[i]==nom:
      res+=1
  return res