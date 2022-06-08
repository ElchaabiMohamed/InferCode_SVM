def suiteAri(liste):
    res=True
    if len(liste) > 1:
        r,n = liste[1]-liste[0],1
        while n<len(liste) and res:
            if liste[n]!=liste[n-1]+r:res=False
            n+=1
    return res
