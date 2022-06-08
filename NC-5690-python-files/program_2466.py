def produitScalaire(vec1,vec2):
  if vec1==[] and vec2==[]:
    res=0
  else:
    res=0
    for i in range(len(vec1)):
      res=res+vec1[i]*vec2[i]
  return res
      