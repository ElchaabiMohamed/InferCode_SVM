def meilleurScoreJoueur(scores,joueurs,nom):
    trouve=False
    i=0
    while i<len(scores) and i<len(joueurs) and trouve:
      if joueurs[i]==nom:
        trouve=True
      i+=1
    if trouve:
      res=scores[i-1]
    else:
      res=0
    return res