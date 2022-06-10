def fibonacci(n):
    if n == 0 or n == 1:
        return 1
    else:
      return fibonacci(n-1) + fibonacci(n-2)

def main():
  a=fibonacci(8)
  print (a)


if __name__=="__main__":
  main()
