def listeDecroissante(scores):
  c=True
  i=0
  while i<(len(score)-1) and c:
    if score[i]<score[i+1]:
      c=False
    i=i+1
  return c      