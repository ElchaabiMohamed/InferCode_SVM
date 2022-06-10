def countdown(num):
  import time
  if num == 0:
    print('LIFT OFF!')
  else:
    print(num)
    time.sleep(0.1)
    countdown(num-1)
  
def search(string, letter):
  if string == []:
    return 'False'
  elif string[0] == letter:
    return 'True'
  else:
    search(string[1:], letter)
  
def index(string,letter):
  position = 0
  if string == []:
    return '-1'
  elif string[0] == letter:
    return position
  else:
    position += 1
    index(string[1:],letter)
  
def fibonacci(n):
  n1 = 0
  n2 = 1
  count = 0
  while count < n:
    if n == 0:
      print(n1)
    elif n == 1:
      print(n2)
    else:
      print(n1)
      print(n2)
  
  
if __name__ == '__main__':
  countdown(3)
  search('niamh','a')
  index('niamh','a')