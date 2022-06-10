#recursive means the function keeps going
#by calling itself until it has reached a conclusion.

def power(m,n):
   if n == 0:
      return 1
   if n == 1:
      return m
   if m == 0:
      return 0
   if m == 1:
      return 1

   return m ** n
   

#from power_102 import power

def main():
   print((power(2,3)))
   print((power(4,4)))
   print((power(2,32)))
   print((power(10,3)))
   print((power(8,0)))

if __name__ == '__main__':
   main()