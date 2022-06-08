def premiereOccurrenceLettre(lettre,mot):
  res=0
  for elem in mot:
    if elem==lettre:
      res=mot[elem]
  return res