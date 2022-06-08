def premiereOccurrenceLettre(lettre,mot):
  res=0
  for i in range(len(mot)):
    if mot[i]==lettre:
      res=i
  return res