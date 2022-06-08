def premiereOccurrenceLettre(lettre,mot):
  if mot=='':
    cpt=none
  else:
    cpt=-1
    for i in range(len(mot)):
      if mot[i]!=lettre:
        cpt=cpt+1
        return cpt
  