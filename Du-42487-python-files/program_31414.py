def overlap(d1=0, d2=0, d3=1, d4=0, d5=0, d6=1):
    r=d3+d6
    r=r**2
    x=(d1-d4)**2
    y=(d2-d5)**2
    d=x+y
    if r > d:
        return (True)
    else:
        return(False)

