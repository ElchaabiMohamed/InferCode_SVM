import sys,math

def overlap(x1 = 0, y1 = 0, r1 = 1, x2 = 0, y2 = 0, r2 = 1):
   dist = math.sqrt(((x2-x1)**2)+((y2-y1)**2)) #this is the dist between two points formula
   if dist - r1 - r2 < 0: #from dist subtract radii to get overlap.
      return True # overlaps if less than 0
   else:
      return False #no overlap



#from circle_62 import overlap

# def main():
#     print(overlap())
#     print(overlap(10))
#     print(overlap(10,10))
#     print(overlap(10,10,10))
#     print(overlap(10,0,10))
#     print(overlap(10,0,1,8,0,1))
#     print(overlap(10,0,1,8,0,2))

# if __name__ == '__main__':
#     main()