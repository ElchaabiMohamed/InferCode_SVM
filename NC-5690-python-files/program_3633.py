def permutationChaine(s):
  res=''
  for i in range (0,len(s)-1,2):
    res=res+s[i+1]+s[i]
  
  return res

