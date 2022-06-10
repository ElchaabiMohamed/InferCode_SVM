def countdown(num):
  import time
  while num != 0:
    print(num)
    num = num - 1
    time.sleep(0.1)
  print('LIFT OFF!')

def search(str,letter):
  if letter in str:
    return 'True'
  else:
    return 'False'
  
def index(str,letter):
  i = 0
  while i < len(str):
    position = 0
    if letter in str:
      position += 1
      return position
    else:
      return '-1'

def fibonacci(n):
  if n == 0:
    return 0
  elif n == 1:
    return 1
  elif n > 1:
    number = 0
    first_num = 1
    second_num = 2
    for n in range(3, n):
      number = first_num * second_num
      first_num = second_num
      second_num = number
    return number
  else: 
    return -1
