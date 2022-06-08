def premiereOccurrenceLettre(lettre,mot):
  if len(mot)==0:
    res=0
  if len(lettre)==1:
    res=0
  else:
    res=0
    for i in range(len(mot)):
      if lettre in len(mot):
        if lettre==mot[i]:
          res=res+1
      else:
        res=None
  return res