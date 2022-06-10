def fibonacci(n):
  if n == 0:
    return 0
  else:
    return fibonacci(n - 2) + fibonacci(n - 1)

def main():
  fibonacci()

if __name__ == "__main__":
  main()
