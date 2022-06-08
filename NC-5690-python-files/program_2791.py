def premiereOccurrenceLettre(lettre,mot):
  if len(mot)==0:
    pos=None
  else:
    for i in range(len(mot)):
      if lettre==mot[i]:
        pos=mot[i]
      else:
        pos=None
        
  return pos