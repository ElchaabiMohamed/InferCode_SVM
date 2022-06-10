def overlap(x1,y1,r1,x2,y2,r2):  
     dist = math.sqrt(x2 - x1)**2 + (y2 - y1)**2  
     if dist < (r1 + r2):
     	return True
     else:
     	return False

