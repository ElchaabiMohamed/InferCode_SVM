def produitScalaire(vec1,vec2):
  for i in range(len(vec1),len(vec2)):
    res=res+(vec1[i]*vec2[i])
  return res