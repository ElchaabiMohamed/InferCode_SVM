def produitScalaire(vec1,vec2):
  res=0
  for i in range(3):
    v1=vec1[i]
    v2=vec2[i]
    res=res+v1*v2
  return res