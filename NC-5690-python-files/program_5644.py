def compare(chaine1,chaine2):
  res=0
  i=0
  while i<len(ch1) and i<len(ch2) and res==0:
    if ch1[i] > ch2[i]:
      res=-1
    elif ch1[i] < ch2[i]:
      res=1
    i=i+1
  return res