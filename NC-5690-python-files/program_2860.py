def doubleLettre(mot):
  res=0
  prec=''
  for c in mot:
    if prec==c:
      dL=True
    else:
      dL=False
    prec=c
  if dL==True:
    res=True
  else:
    res=False
  return res