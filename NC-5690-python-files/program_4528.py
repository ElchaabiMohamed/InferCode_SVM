def meilleurScoreJoueur(score,joueur):
  i=0
  if joueur[i] not in joueur:
    return 0
  else:
    while i<len(joueur)-1:
      if score[i+1]>score[i]:
        return joueur[i+1]
    i=i+1
  return joueur
