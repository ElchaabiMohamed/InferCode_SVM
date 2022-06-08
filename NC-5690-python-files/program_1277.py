def produitScalaire(vec1,vec2):
  res=0
  for i in range(len(vec1) and len(vec2)):
    res=res+vec1[i]*vec2[i]
  return res