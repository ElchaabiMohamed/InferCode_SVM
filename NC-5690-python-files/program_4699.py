def motPalindrome(mot):
    if mot=='':
      ok=True
    else:
      ok=True
      i=0
      while i<len(mot) and ok:
        if mot[i]!=mot[-i-1]:
          ok=False
        i+=1
    return ok
      