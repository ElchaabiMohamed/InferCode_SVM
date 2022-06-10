def power(m, n):
   if n == 0:
      return 1
   else:
      return power(m , n - 1) * m

def main():
    print((power(2,2)))

if __name__ == '__main__':
    main()