def prononcable(mot):
  voyelle=0
  consonne=0
  for elem in mot:
    if elem in 'aeiouy':
      voyelle+=1
    else:
      consonne+=1
    if voyelle==3 or consonne==3:
      return False
  return True