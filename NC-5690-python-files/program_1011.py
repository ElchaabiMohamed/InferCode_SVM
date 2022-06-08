def phrasePalindrome(phrase):
    if phrase=='':
      ok=True
    else:
      liste=[]
      for c in phrase:
        liste.append(c)
      palindrome=[]
      for c in liste:
        if c!=' ':
          palindrome.append(c)
      ok=True
      i=0
      while i<len(palindrome) and ok:
        if palindrome[i]!=palindrome[-i-1]:
          ok=False
        i+=1
    return ok