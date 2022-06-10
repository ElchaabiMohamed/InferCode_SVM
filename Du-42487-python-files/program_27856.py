def selectionsort(l):
  N = len(l)
  p = 0
  j = 1
  while j < N:
    if l[j] < l[p]:
      p = j
    j += 1
  return p

def main():
  selectionsort()

if __name__ == "__main__":
  main()
