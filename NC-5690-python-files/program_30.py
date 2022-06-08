def nbOccurrencesJoueur(joueurs,nom):
  cpt=0
  i=0
  while i<len(joueurs):
    if nom==joueurs[i]:
      cpt=cpt+1
    i=i+1
  return cpt