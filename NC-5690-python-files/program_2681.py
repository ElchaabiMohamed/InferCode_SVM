def premiereOccurrenceLettre(lettre,mot):
  for i in range(len(mot)):
    if mot[i]==lettre:
      return i
  