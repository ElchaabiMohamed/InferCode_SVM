def nbOccurrencesJoueur(joueurs,nom):
    cpt=0
    i=0
    while i<len(joueurs):
      if joueurs[i]==nom:
        cpt+=1
      i+=1
    return cpt
  