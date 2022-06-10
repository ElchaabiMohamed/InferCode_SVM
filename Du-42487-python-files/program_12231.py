def countdown(num):
  import time
  if num == 1:
    print('1')
    time.sleep(0.1)
    print('LIFT OFF!')
  else:
    print(num)
    time.sleep(0.1)
    countdown(num - 1)

def search(str,letter):
  if str == "":
    return False
  elif str[0] == letter:
    return True
  else:
    return search(str[1:], letter)

def index(str,letter):
  position = 0
  if position == len(str):
    return '-1'
  elif str[position] == letter:
    return pos
  else:
    return index(str, letter, position + 1)

#def fibonacci(n):

