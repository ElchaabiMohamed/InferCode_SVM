def nextConway(s):
  res=''
  prec=None
  cpt=0
  for c in s:
    if c==prec:
      cpt+=1
    else:
      if prec:
        res+=str(cpt)+str(prec)
      cpt+=1
    prec=c
  if prec:
    res+=str(cpt)+str(prec)
  return res