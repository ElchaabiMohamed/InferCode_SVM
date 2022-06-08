def produitScalaire(vec1,vec2):
  res=0
  i=0
  while i<len(vec1) and i<len(vec2):
    v1=vec1[i]
    v2=vec2[i]
    res=res+v1*v2
  return res