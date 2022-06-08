def premiereOccurrenceLettre(lettre,mot):
  if len(mot)==0:
    res=None 
  else:
    res=None
    for i in mot: 
      if lettre==mot[i]:
        res=i
  return res