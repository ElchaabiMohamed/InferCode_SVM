def sommeNPremiersEntiersPairs(n):
    res=0
    for x in range(1,n+1,2):
        if x%2==0:
            res=res+x        
    return res