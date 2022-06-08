def premiereOccurrenceLettre(lettre,mot):
    if len(mot)==0 or lettre not in mot:
      res=None
    else:
      res=0
      cpt=0
      for i in range(len(mot)):
        if mot[i]==lettre:
          cpt+=1
          res=i
    return res