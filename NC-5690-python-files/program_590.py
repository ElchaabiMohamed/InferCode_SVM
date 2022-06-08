def produitScalaire(l1,l2):
  res=0
  i=0
  while i<len(l1) and i<len(l2):
    res=res+(l1[i]*l2[i])
    i+=1
  return res