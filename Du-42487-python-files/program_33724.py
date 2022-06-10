def overlap(x1=0,y1=0,r1=0,x2=0,y2=0,r2=1):
    distanceX = x1 - x2;
    distanceY = y1 - y2;
    radiusSum = r1 + r2;
    return distanceX * distanceX + distanceY * distanceY <= radiusSum * radiusSum;
