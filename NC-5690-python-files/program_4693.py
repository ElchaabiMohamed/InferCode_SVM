def nbOccurrencesJoueur(joueurs,nom):
  cpt=0
  for elem in joueurs:
    if elem==nom:
      cpt+=1
  return cpt