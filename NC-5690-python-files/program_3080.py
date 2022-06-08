def meilleurScoreJoueur(scores,joueurs,nom):
  score = 0
  i = 0
  while i < len(scores) and score == 0:
    if nom == joueurs[i] :
      score = scores[i]
    i = i + 1
  return score