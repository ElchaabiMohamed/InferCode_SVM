def nbOccurrencesJoueur(joueurs,nom):
  cpt=0
  for i in range(len(joueurs)):
    if joueurs[i]==nom:
      cpt+=1
  return cpt