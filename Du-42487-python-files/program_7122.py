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
 
    