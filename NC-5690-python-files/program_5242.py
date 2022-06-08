def premiereOccurrenceLettre(lettre,mot):
  res=0
  for i in range(0,len(mot)):
    if mot[i]==lettre:
      res=i
  return res