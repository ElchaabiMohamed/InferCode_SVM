import time

def countdown(num):
  if num == 1:
    print(num)
  else:
    print(num)
    time.sleep(0.1)
    countdown(num - 1)