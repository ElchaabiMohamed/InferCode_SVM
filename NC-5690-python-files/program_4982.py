def listeDecroissante(scores):
  res=True
  if len(scores)==0:
    return res
  else:
    x=True
    i=0
    while i<len(scores) and x:
      if scores[i]<scores[i+1]:
        x=False
      i=i+1
    return x