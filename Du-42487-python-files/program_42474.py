import math

def overlap(x1=0, y1=0, r1=1, x2=0, y2=0, r2=1):
  dist = math.sqrt((x2 - x1) ** 2 + (y2 - y1) **2)
  return abs(r1 - r2) <= dist <= abs(r1 + r2) and ((r1 > (dist + r2)) or (r2 > (dist + r1)))

def main():
  pass

if __name__ == "__main__":
  main()
