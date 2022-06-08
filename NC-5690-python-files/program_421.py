def prononcable(mot):
  for i in range(len(mot)-2):
    if mot[i] in 'aeiouy' and mot[i+1] in 'aeiouy' and mot[i+2] in 'aeiouy':
      return False
    elif mot[i] in 'bcdfghjklmnpqrstvwxz' and mot[i+1] in 'bcdfghjklmnpqrstvwxz' and mot[i+2] in 'bcdfghjklmnpqrstvwxz':
      return False
    else:
      return True