def countdown(num):
  import time
  while num > 0:
    print(num) 
    time.sleep(0.1)
    num -= 1
  print("LIFT OFF!")

def search(str, letter):
  if letter in str:
    print("True".rstrip())
  else:
    print("False".rstrip())
