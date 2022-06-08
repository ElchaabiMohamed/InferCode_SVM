def meilleurScoreJoueur(score,joueurs,nom):
  res=0
  trouve=False
  i=0
  while i<len(score) and not trouve:
    if nom==listejoueur[i]:
       res=score[i]
       trouve=True     
    i=i+1
  return res