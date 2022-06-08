def premiereOccurrenceLettre(lettre,mot):
  res=0
  for i in mot:
    if mot[i]==lettre:
      res=i
  return res