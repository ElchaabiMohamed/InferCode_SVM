def selectionsort(a):
  j = 0
  i = 1
  while i < len(a):
    if a[i] < a[j]:
      j = i
    i += 1
  return a

def main():
  selectionsort()

if __name__ == "__main__":
  main()
