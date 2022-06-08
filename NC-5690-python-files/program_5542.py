def produitScalaire(vec1,vec2):
  res=0
  vec3=[0]*len(vec1)
  for i in range(len(vec1)):
    vec3[i]=vec1[i]*vec2[i]
  for elem in vec3:
    res+=elem
  return res