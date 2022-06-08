def motPalindrom(mot):
  i=0
  res=True
  while i<len(mot) and res==True:
    pl=mot[i]
    dl=mot[i-1]
    if pl==dl:
        res=True
    else:
        res=False
    i+=1
  return res