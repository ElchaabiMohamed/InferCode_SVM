def listeDecroissante(scores):
  i=0
  while i<len(scores)-1:
    if scores[i]<scores[i+1]:
      return False
    i+=1
  return True