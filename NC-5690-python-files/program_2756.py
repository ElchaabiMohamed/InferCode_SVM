def prononcable(mot):
    ok=True
    voy=0
    csn=0
    i=0
    while i<len(mot) and voy<4 and csn<4:
      if mot[i] in 'aeiouy':
        voy+=1
        csn=0
      else:
        csn+=1
        voy=0
      i+=1
    if voy>3 or csn>3:
      ok=False
    return ok