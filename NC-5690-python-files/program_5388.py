def listeDecroissante(scores):
  for i in range(len(scores)-1):
    if scores[i]<scores[i+1]:
      return False
  return True