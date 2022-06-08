def phrasePalindrome(phrase):
  ok=True
  i=0
  sansespace=''
  for lettre in phrase:
    if lettre!=' ':
      sansespace+=lettre
  while i<len(sansespace)/2 and ok:
    ok=sansespace[i]==sansespace[i-1]
    i+=1
  return ok
