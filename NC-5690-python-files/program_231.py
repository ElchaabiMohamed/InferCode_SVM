def sousChaine(s1,s2):
    if s1=='':
      ok=True
    elif s2=='':
      ok=False
    else:
      ok=False
      cpt=0
      i=0
      j=0
      while i<len(s1) and j<len(s2) and not ok:
        if s1[i]==s2[j]:
          cpt+=1
          i+=1
          j+=1
        else:
          cpt=0
          i=0
          j+=1
        if cpt==len(s1):
          ok=True
    return ok