def countdown(num):
  import time
  i = 0
  while i < int(num):
    print(int(num) - i)
    time.sleep(0.1)
    i = i + 1
  print('LIFT OFF!')

def search(string,letter):
  return letter in string

def index(string,letter):
  position = -1
  i = 0
  while i < len(string):
    if string[i] == letter:
      position = i
    i = i + 1
  return position
     

#def fibonacci(n):
 # total = 0
  #i = 0
  #while i < int(n):
   # total = 

if __name__ == '__main__':
  countdown(3)
  search('niamh','a')
  index('niamh','a')
