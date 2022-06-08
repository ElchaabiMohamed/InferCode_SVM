def phrasePalindrome(phrase):
    if phrase=='':
      ok=True
    else:
      ok=True
      i=0
      while i<len(phrase) and ok:
        if phrase[i]!=phrase[-i-1]:
          ok=False
        i+=1
    return ok