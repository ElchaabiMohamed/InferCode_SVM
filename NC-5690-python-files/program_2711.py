def moyenne(liste):
  if len(liste)!=0:
    num=0
    for elem in liste:
  	  num+=elem
    res=num/len(liste)
    return res
    