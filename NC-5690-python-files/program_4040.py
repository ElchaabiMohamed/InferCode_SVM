def produitScalaire(vec1,vec2):
  res=0
  for i in range(4):
    e1=vec1[i]
    e2=vec2[i]
    res=res+e1*e2
  return res