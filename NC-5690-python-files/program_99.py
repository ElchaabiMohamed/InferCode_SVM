def listeDecroissante(scores):
   for i in range(len(scores)):
      if scores[i]<scores[i+1]:
        return False
      else: 
        return True