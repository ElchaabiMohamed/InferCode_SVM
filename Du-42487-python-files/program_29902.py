import time


def countdown(num):
  i=num
  while i>0:
    print(i)
    time.sleep(0.1)
    i=i-1
  print("LIFT OFF!")
