def overlap(d1=0, d2=0, d3=1, d4=0, d5=0, d6=1):
    import math
    r=d3+d6
    d=(d1-d4)**2-(d2-d5)**2
    d=math.sqrt(d)
    if r >= d:
        return (True)
    else:
        return(False)

