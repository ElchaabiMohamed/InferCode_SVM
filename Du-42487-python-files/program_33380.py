def countdown(num):
  import time
  while num > 0:
    print(num) 
    time.sleep(0.1)
    num -= 1
  print("LIFT OFF!")

def search(str, letter):
  i = 0
  while i < len(str):
    if letter == str[i]:
      print("True")
    else:
      print("False")
    i += 1
