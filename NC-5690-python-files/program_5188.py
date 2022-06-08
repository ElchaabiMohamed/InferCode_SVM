def produitScalaire(L1,L2):
  res=0
  if len(L1)!=len(L2):
    res=None
  else:
    for i in range (len(L1)):
      res=res+L1[i]*L2[i]
  return res