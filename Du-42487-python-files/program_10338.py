import time

def countdown(num):
  if num == 1:
    print(num)
    time.sleep(0.1)
    print("LIFT OFF!")
  else:
    print(num)
    time.sleep(0.1)
    countdown(num - 1)

if __name__ == '__main__':
  print(countdown(4))

def search(str,letter):
  if str == []:
    return False
  elif lstr[0] == letter:
    return True
  else:
    return search(str[1:],letter)

if __name__ == '__main__':
  print(search(abcd,a))
    
def index(str,letter,pos):
  if pos == len(str):
    return -1
  elif str[pos] == letter:
    return pos
  else:
    return index(str,letter,pos + 1)

if __name__ == '__main__':
  print(index(abcd,a))

def fibonacci(n):
  if n <= 1:
    return n
  else:
    return fibonacci(n-1) + fibonacci(n-2)

if __name__ == '__main__':
  print(fibonacci(3))


































