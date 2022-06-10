def countdown(num):
  import time
  if num == 0:
    print('LIFT OFF!')
  else:
    print(num)
    time.sleep(0.1)
    countdown(num-1)
  
def search(string, letter):
  if string == "":
    return 'False'
  elif string[0] == letter:
    return 'True'
  else:
    return search(string[1:], letter)
  
def index(string,letter,position):
  if string == "":
    return '-1'
  elif string[0] == letter:
    return position
  else:
    position += 1
    return index(string[1:],letter,position)
  
def fibonacci(n):
  time = 0
  if n <= 1:
    return n
  else:
    return (fibonacci(n-1) + fibonacci(n-2))
  
if __name__ == '__main__':
  countdown(3)
  search('niamh','a')
  index('niamh','a')