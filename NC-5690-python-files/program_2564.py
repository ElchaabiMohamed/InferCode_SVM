def permutationChaine(s):
    res=''
    for i in range(0,len(s)-1,len(s)):
        res=res+s[i]
    return res