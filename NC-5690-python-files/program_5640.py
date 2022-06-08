def motPalindrome(mot):
    if len(mot)==0:
      res=True
    else:
      ok=True
      i=0
      while i<len(mot) and ok:
        ok=mot[i]==mot[-1]
        i+=1
      res=ok
    return res