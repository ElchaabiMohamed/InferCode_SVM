def premiereOccurrenceLettre(lettre,mot):
  for i in range(len(mot)):
    if lettre == mot[i]:
      return i
  return None
