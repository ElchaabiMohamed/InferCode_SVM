def nbOccurrencesJoueur(joueurs,nom):
  i=0
  cpt=0
  while i<len(joueurs):
    if nom==joueurs[i]:
      cpt=cpt+1
    i=i+1
  return cpt