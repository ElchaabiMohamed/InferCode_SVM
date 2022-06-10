import time
  
def countdown(num):
   '''prints all the numbers from num to 1 with a gap of 100 milliseconds in between each print, followed by LIFT OFF!'''
   while num >= 1:
     print(num)
     time.sleep(0.1)
     num = num - 1
   print('LIFT OFF!')
  
def search(str,letter):
    '''returns True if letter is in str, False if it is not there'''
    i = 0
    while i < len(str):
      if letter == str[i]:
        return True
      i = i + 1
    return False
  
def index(str,letter):
    '''returns the position of letter in str, -1 if it is not there'''
    i = 0
    while i < len(str):
      if letter == str[i]:
        return i
      i = i + 1
    return -1
  
  
def fibonacci(n):
    '''returns the value of the fibonacci series at position n'''
    if n == 0:
      return 0
    if n == 1:
      return 1
    else:
      fibN_2 = 0
      fibN_1 = 1
      i = 2
      while i <=n:
        fibN = fibN_2 + fibN_1
        fibN_2 = fibN_1
        fibN_1 = fibN
        i = i + 1
      return fibN
  
if __name__ == '__main__':
    print('testing countdown')
    countdown(10)
  
    print('testing search')
    print(search('test','t'))
    print(search('test','a'))
  
    print('testing index')
    print(index('test','t'))
    print(index('test','a'))
  
    print('testing fibonacci')
    print(fibonacci(5))


















































































