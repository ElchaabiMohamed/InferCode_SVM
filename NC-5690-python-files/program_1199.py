def motPalindrome(mot):
    if len(mot)==0:
      res=True
    else:
      res=True
      i=0
      while i<len(mot) and res:
        res=mot[i]==mot[-1]
        i+=1
    return res
