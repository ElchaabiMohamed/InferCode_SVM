def motPalindrome(mot):
    if len(mot)==0:
      res=True
    else:
      res=True
      i=0
      while i<len(mot) and res:
        if mot[i]==mot[-i-1]:
          res=True
        i+=1
    return res