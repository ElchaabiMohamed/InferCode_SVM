def countdown(num):
   import time
   while num >=  1:
      print(num)
      time.sleep(0.1)
      num = num - 1
   print("LIFT OFF!")
   
if __name__ == "__main__":
   print('Calling countdown function.')
   countdown(3)
   
def search(str,letter):
   i = 0
   while i < len(str):
      if str[i] == letter:
         return True
      i = i + 1
   return False
   
if __name__ == "__main__":
   print('calling search function')
   print(search('test', 'e'))
   print(search('test', 'a'))
   
def index(str,letter):
   i = 0
   while i < len(str):
      if str[i] == letter:
         return i
      i = i + 1
   return '-1'
   
if __name__ == '__main__':
   print('calling index function.')
   print(index('python', 'i'))
   print(index('python', 'o'))
   
def fibonacci(n):
   firN = 0
   secN = 1
   while n > 0:
      prev_N = firN
      firN = secN
      sec_N = prev_N + secN
      n -= 1
   return firN
   
if __name__ == '__main__':
   print('calling fibonacci function')
   print(fibonacci(0))
   print(fibonacci(6))
   
   
      