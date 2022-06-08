def phrasePalindrome(phrase):
    if len(phrase)==0:
      res=True
    else:
      res=True
      i=0
      x=phrase-''
      while i<len(phrase)//2 and res and x:
        if phrase[i]!=phrase[-(i+1)]:
          res=False
        if phrase[i]=='':
            res=False
        i+=1
    return res