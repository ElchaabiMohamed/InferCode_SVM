def motPalindrome(mot):
    if len(mot)==0:
      res=True
    else:
      res=True
      i=0
      while i<len(mot) and res==True:
        if mot[i//2]==mot[-i//2]:
          res=True
          i+=1
        if mot[i//2]!=mot[-i//2]:
          res=False
    return res