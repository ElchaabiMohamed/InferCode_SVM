def swap(a, i, j):
  tmp = a[i]
  a[i] = a[j]
  a[j] = tmp

def reverse(a):
  return swap(a)

def main():
  print(swap(a, i, j))
  print(reverse(a))

if __name__ == "__main__":
  main()
