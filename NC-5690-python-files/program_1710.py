def permutationChaine(s):
  res=""
  for i in range(0,len(s),2):
    x=s[i]
    s[i]=s[i+1]
    s[i+1]=x
    res=res+s[i]+s[i+1]
  return res
