def nbOccurrencesJoueur(joueurs,nom):
  cpt = 0
  for i in joueurs:
    if i == nom:
      cpt+=1
  return cpt