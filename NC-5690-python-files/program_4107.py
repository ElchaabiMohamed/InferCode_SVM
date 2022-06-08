def produitScalaire(vec1,vec2):
  res=0
  for i in range(0,4):
    res=(vec1[i]*vec2)+res
  return res