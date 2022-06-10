import math

def overlap(x1=0, y1=0, r1=1, x2=0, y2=0, r2=1):
  dist = math.sqrt((x2 - x1) ** 2 + (y2 - y1) **2)
  internal = r1 + r2
  external = r1 - r2
  return (internal == dist) or (external == dist)

def main():
  pass

if __name__ == "__main__":
  main()
