def phrasePalindrome(phrase):
    if len(phrase)==0:
      res=True
    else:
      res=True
      i=0
      x=''
      while i<len(phrase)//2 and res:
        if phrase[i]==x:
          i+=2
        else:
          if phrase[i]!=phrase[-(i+1)]:
            res=False
        i+=1
    return res