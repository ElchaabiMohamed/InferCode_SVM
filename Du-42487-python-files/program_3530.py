import sys



def overlap(x1=0,y1=0,r1=0,x2=0,y2=0,r2=0):
    distance = ((x1-x2)**2) + ((y1 - y2)**2)
    radii = r1 + r2
    return distance > radii
    