import time

def countdown(num):
  '''prints all the numbers from num to 1 with a gap of 100 milliseconds in between each print, followed by LIFT OFF!'''
  if num == 0:
    print("LIFT OFF!")
  else:
    print(num)
    time.sleep(0.1)
    countdown(num-1)

def search(str,letter):
  '''returns True if letter is in str, False otherwise'''
  if str == "":
    return False
  elif str[0] == letter:
    return True
  else:
    #keep looking
    return search(str[1:],letter)
  

def index(str,letter,pos):
  '''returns the position of letter in str, -1 if it is not there'''
  if pos == len(str):
    return -1
  elif str[pos] == letter:
    return pos
  else:
    return index(str,letter,pos+1)


def fibonacci(n):
  '''returns the value of the fibonacci series at position n'''
  if n == 0:
    return 0
  elif n == 1:
    return 1
  else:
    return fibonacci(n-1) + fibonacci(n-2)

if __name__ == '__main__':
  print('testing countdown')
  countdown(10)

  print('testing search')
  print(search('test','t'))
  print(search('test','a'))

  print('testing index')
  print(index('test','t',0))
  print(index('test','a',0))

  print('testing fibonacci')
  print(fibonacci(5))

   
    


