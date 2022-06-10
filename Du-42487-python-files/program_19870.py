def overlap(d1=0, d2=0, d3=0, d4=0, d5=0, d6=0):
    r=d3+d6
    d=((d1-d4)*(d1-d4))-((d2-d5)*(d2-d5))
    if r >= d:
        return (True)
    else:
        return(False)

