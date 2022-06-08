def motPalindrom(mot):
  i=0
  if len(mot)==0:
    res=True
  else:
    while i<len(mot):
      pl=mot[i]
      dl=mot[i-1]
      if pl==dl:
        res=True
      else:
        res=False
      i+=1
  return res