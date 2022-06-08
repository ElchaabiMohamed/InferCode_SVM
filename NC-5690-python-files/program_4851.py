def nbOccurrencesJoueur(joueurs,nom):
  cpt=0
  for i in range(len(joueurs)):
    if nom==joueurs[i]:
      cpt+=1
  return cpt