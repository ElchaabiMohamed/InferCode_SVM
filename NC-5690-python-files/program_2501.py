def motPalindrome(mot):
    if len(mot)==0:
      res=True
    else:
      res=True
      i=0
      while i<len(mot) and res==True:
        if mot[i]==mot[-i]:
          res=True
        i+=1
    return res
