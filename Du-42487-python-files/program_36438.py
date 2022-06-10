def countdown(num):
  import time
  while num != 0:
    print(num)
    num = num - 1
    time.sleep(0.1)
  print('LIFT OFF!')

def search(str,letter):
  for letters in str:
    if letters in str:
      print('True')
    else:
      print('False')

