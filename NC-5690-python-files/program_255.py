def listeDecroissante(scores):
  if scores==[]:
    return True
  else:
   for i in range(len(scores)):
      if scores[i]<scores[i+1]:
        return False
      else: 
        return True