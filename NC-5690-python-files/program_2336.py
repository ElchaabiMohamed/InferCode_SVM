def permutationChaine(s):
    res=''
    for i in range(0,len(s)-1,2):
        res=res+s[i+1]+s[i]
    if res%2!=0:
        res=res+len(s)
    return res