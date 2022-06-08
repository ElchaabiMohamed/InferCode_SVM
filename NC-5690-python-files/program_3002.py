def premiereOccurrenceLettre(lettre,mot):
  if mot=='':
    cpt=None
  else:
    cpt=0
    for i in range(len(mot)):
      if mot[i]!=lettre:
        cpt=cpt+1
      else:
        return cpt
  