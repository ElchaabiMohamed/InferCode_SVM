def premiereOccurrenceLettre(lettre,mot):
    trouve=False
    i=0
    while i<len(mot) and not trouve:
      if mot[i]==lettre:
        ok=True
      i+=1
    if trouve==True:
      i-=1
    if trouve==False:
      i=None
    return i