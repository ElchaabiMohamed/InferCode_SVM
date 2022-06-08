def doubleLettre(mot):
  res=0
  dL=0
  prec=''
  for c in mot:
    if prec==c:
      dL=True
    else:
      dL=False
    prec=c
  if dL==True:
    res=True
  return res