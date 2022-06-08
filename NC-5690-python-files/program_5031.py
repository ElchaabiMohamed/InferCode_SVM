def prononcable(mot):
  if len(mot)==0:
    return True
  for lettre in mot:
    if lettre=='aeiouy' and lettre!=3*lettre:
      return True
    else:
      if lettre!='aeiouy' and lettre!=3*lettre:
        return False