def premiereOccurrenceLettre(lettre,mot):
    res=None
    i=0
    while i<len(mot) and res:
      if lettre==mot[i]:
        res=i
      i+=1
    return res