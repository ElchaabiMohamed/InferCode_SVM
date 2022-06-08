def nbSyllabes(mot):
  if mot=='':
    res=0
  else:
    res=0
    Voyelles=['aeiouy']
    ch=""
    for i in range(1,len(mot)):
      if mot[i-1] not in Voyelles and mot[i] in Voyelles:
        res=res+1
    if mot[0] in Voyelles :
      res=res+1
    elif mot[-1] not in Voyelles:
      res=res-1
    else:
      if res==0:
        res=res+1
  return res