import time
 
def countdown(num):
  while num >= 1 :
    print(num)
    time.sleep(0.1)
    num = num - 1
  print("LIFT OFF!")
 
if __name__ == '__main__':
  print(countdown(4))
 
def search(str,letter):
  i = 0
  while i < len(str):
    if str[i] == letter:
      return True
    i = i + 1
  return False
 
if __name__ == '__main__':
  print(search(abcd,a))

def index(str,letter):
  i = 0
  while i < len(str) and str[i] != letter:
    i = i + 1
  if i < len(str):
    return i
  else:
    return "-1" 

if __name__ == '__main__':
  print(index(abcd,a))

def fibonacci(n):
  a = 0
  b = 1
  while n > 0:
    prev_a = a
    a = b
    b = prev_a + b
    n -= 1
  return a

if __name__ == '__main__':
  print(fibonacci(3))







