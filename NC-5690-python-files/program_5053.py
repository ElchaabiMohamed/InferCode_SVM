def meilleurScoreJoueur(scores,joueurs,nom):
  if nom not in joueurs:
    mSJ=0
  else:
    mSJ=None
    for i in range(len(joueurs)):
      if scores[i]>mSJ and joueurs[i]==nom:
        mSJ=scores[i]
  return mSJ