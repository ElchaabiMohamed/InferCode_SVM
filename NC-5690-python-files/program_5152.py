def sousChaine(s1,s2):
  Trouve=False
  i=0
  while i<len(s1) and i<len(s2):
    ok=False
    if s1 in s2:
      Trouve=True
    i=i+1
  if s1=='':
    Trouve=True
  return Trouve
