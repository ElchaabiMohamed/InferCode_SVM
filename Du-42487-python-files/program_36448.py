def power(m, n):
  while n > 0:
    m = m * m
    n = n - 1
  return m

def main():
  power()

if __name__ == "__main__":
  main()
