def sousChaine(s1,s2):
  Trouve=False
  i=0
  if s1=='':
    Trouve=True
  while i<len(s1) and i<len(s2):
    ok=False
    if s1 in s2:
      Trouve=True
    i=i+1
  return Trouve
