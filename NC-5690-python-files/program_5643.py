def listeDecroissante(scores):
  res=True
  i=0
  while i<len(score)-1:
    if score[i]<score[i+1]:
      return False
    i=i+1
  return res