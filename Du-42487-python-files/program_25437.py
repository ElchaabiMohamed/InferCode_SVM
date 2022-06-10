def countdown(num):
  import time
  if num == 1:
    print(num)
    return 'LIFT OFF!'
  else:
    print(num)
    countdown(num-1)
    time.sleep(0.1)
  

def search(string,letter):
  if letter == string:
    return 'True'
  else:
    search(string[1:],letter)
  return 'False'
  

def index(string,letter):
  position = -1
  i = 0
  while i < len(string):
    if string[i] == letter:
      position = i
    i = i + 1
  return position
     

def fibonacci(n):
  total = 0
  n0 = 0
  n1 = 1
  if n == 0:
    total = n0
    return total
  elif n == 1:
    total = n1
    return total
  else:
    while total < n:
      n = n0 + n1
      n0 = n1
      n1 = n
      total = total + 1
    return total


if __name__ == '__main__':
  countdown(3)
  search('niamh','a')
  index('niamh','a')
  fibonacci(3)
