def produitScalaire(vec1,vec2):
  res=0
  for i in range(len(vec1)):
    res=vec1[i]*vec2[i]+res
  return res