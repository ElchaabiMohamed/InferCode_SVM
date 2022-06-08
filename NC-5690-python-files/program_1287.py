def premiereOccurrenceLettre(lettre,mot):
  for i in range(mot):
    if mot[i]==lettre:
      res=i
    else:
      res=None
  return res