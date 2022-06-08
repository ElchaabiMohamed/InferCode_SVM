def premiereOccurrenceLettre(lettre,mot):
  if mot=='':
    pos=None
  else:
    for i in range(len(mot)):
      if lettre==mot[i]:
        pos=i
        return pos