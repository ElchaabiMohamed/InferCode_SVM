def premiereOccurrenceLettre(lettre,mot):
  res=[]
  for i in range(0,len(mot)):
    if mot[i]==lettre:
      res=res+mot[i]
  return res