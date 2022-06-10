def power(m, n):
  if n == 0:
    return m
  return m * power(m, n - 1)

def main():
  power()

if __name__ == "__main__":
  main()
