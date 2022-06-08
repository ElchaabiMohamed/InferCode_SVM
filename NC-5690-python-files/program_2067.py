def phrasePalindrome(phrase):
    if len(phrase)==0:
      res=True
    else:
      res=True
      i=0
      x=''
      y=phrase-x
      while i<len(y)//2 and res:
        if y[i]!=y[-(i+1)]:
          res=False
        i+=1
    return res