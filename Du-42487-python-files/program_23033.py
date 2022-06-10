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
