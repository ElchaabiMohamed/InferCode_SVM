def motPalindrome(mot):
    if len(mot)==0:
      res=True
    else:
      res=True
      i=0
      while i<len(mot)//2 and res:
        if mot[i]!=mot[-(i+1)]:
          res=False
        i+=1
    return res