def power(m, n):
  while n != 0:
    m *= m
    n -= 1
  return m

def main():
  power()

if __name__ == "__main__":
  main()
