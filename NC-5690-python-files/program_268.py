def produitScalaire(vec1,vec2):
  res=0
  i=0
  while i<len(vec1) and i<len(vec2) and res==0:
    res=vec1[i]*vec2[i]
    res+=res[i+1]
  return res