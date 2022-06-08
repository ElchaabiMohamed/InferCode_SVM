def produitScalaire(vec1,vec2):
  if vec1 == []:
    coordvec1 = [0,0]
  if vec2 == []:
    coordvec2 = [0,0]
  else :
    coordvec1 = [vec1[2]-vec1[0],vec1[1]-vec1[3]]
    coordvec2 = [vec2[2]-vec2[0],vec2[1]-vec2[3]]
  res = coordvec1[0]*coordvec2[0]+coordvec1[1]*coordvec2[1]
  return res