def phrasePalindrome(phrase):
    if phrase=='':
      ok=True
    else:
      ok=True
      i=0
      j=-1
      while i<len(phrase) and j<len(phrase) and ok:
        if phrase[i]!=phrase[j] and phrase[i]!='' and phrase[j]!='':
          ok=False
        if phrase[i]!='':
          i+=1
        if phrase[j]!='':
          j-=1
    return ok