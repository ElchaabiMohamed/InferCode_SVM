def phrasePalindrome(phrase):
  ok=True
  i=0
  sansespace=''
  #enlever les espaces de la phrases
  for lettre in phrase:
    if lettre!=' ':
      sansespace+=lettre
  #vérifier la symétrie de la phrase
  while i<len(sansespace)//2 and ok:
    ok=sansespace[i]==sansespace[-i-1]
    i+=1
  return ok
