def selectionsort(a):
  i = 0
  while i < len(a):
    p, j = i, i + 1
    while j < len(a):
      if a[j] < a[p]:
        p = j
      j += 1
    a[p], a[i] = a[i], a[p]
    i += 1
  return a

def main():
  selectionsort()

if __name__ == "__main__":
  main()
