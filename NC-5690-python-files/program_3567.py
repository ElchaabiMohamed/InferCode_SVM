def produitScalaire(vec1,vec2):
  res=0
  if len(vec1)!=len(vec2): 
    res=None
  else:
    for i in range(len(vec1)):
      res=res+vec1[i]*vec2[i]
  return res