def maximum(line = []):
   m = line[0]
   for i in line:
      if i > m:
         m = i
   return m

def main():
   max = None
   print((maximum([6,5,1,3,4])))
   print((maximum([6,5,11,3,4])))
   print((maximum([6,15,11,13,14])))
   print((maximum([6,15,11,13,4])))

if __name__ == '__main__':
   main()