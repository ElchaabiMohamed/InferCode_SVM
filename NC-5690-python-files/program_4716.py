def nextConway(s):
  res=''
  cpt=1
  for i in range(len(s)):
    if i==len(s)-1 or s[i+1]!=s[i]:
      res+=str(cpt)+s[i]
      cpt=1
    else:
      cpt+=1
  return res