def motPalindrome(mot):
  i=0
  if len(mot)==0:
    res=True
    good=True
  else:
    while i<len(mot)-1 and good==True:
      l1=mot[i]
      l2=mot[i+1]
      if l1 in 'aeiouy' and l2 in 'bcdfghjklmnpqrstvxz' or l1 in 'bcdfghjklmnpqrstvxz' and l2 in 'aeiouy':
        res=True
      else:
        res=False
        good=False
  return res