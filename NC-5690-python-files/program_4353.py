def phrasePalindrome(phrase):
    if len(phrase)==0:
      res=True
    else:
      res=True
      x=phrase-''
      i=0
      while i<len(phrase)//2 and res and x:
        if phrase[i]!=phrase[-(i+1)] or phrase[i]!='':
          res=False
        i+=1
    return res