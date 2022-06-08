def produitScalaire(vec1,vec2):
  res=0
  for i in range(4):
    res=res+vec1[i]*vec2[i]
  return res