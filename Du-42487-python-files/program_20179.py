import time

def countdown(num):
  while num >= 1:
    print(num)
    time.sleep(0.1)
    num = num - 1
  print('LIFT OFF!')

def search(str,letter):
  i = 0
  while i < len(str):
    if letter == str[i]:
      return True
    i = i + 1
  return False

def index(str,letter):
  i = 0
  while i < len(str):
    if letter == str[i]:
      return i
    i = i + 1
  return -1


def fibonacci(n):
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