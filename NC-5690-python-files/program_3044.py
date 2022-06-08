def produitScalaire(vec1,vec2):
  res=0
  i=0
  while i<len(vec1) and i<len(vec2):
    p1=vec1[i]
    p2=vec2[i]
    res=res+p1*p2
    i=i+1
  return res
