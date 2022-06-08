def permutationChaine(s):
  res=''
  if len(s)<1:
  	res=''
  else:
    for i in range(0,len(s)-1,2):
      res=res+s[i+1]
      res=res+s[i]
  l=s[len(s)]
  res=res+s[l]
  return res